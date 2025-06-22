import torch
from nodes import common_ksampler
from nodes import node_helpers
import nodes
import comfy.model_management

class WanImageToVideoAlt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "length": ("INT", {"default": 81, "min": 1, "max": nodes.MAX_RESOLUTION, "step": 4}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
                 "start_latent": ("LATENT",),
            },
        }

    RETURN_TYPES = ("CONDITIONING", "CONDITIONING", "LATENT")
    RETURN_NAMES = ("positive", "negative", "latent")
    FUNCTION = "encode"

    CATEGORY = "conditioning/video_models"

    def encode(self, positive, negative, length, batch_size, start_latent):
        # Calculate expected temporal dimension
        temp_dim = ((length - 1) // 4) + 1
        concat_latent_image = start_latent["samples"]
        width = concat_latent_image.shape[-1]
        height = concat_latent_image.shape[-2]
        
        latent = torch.ones([batch_size, 16, temp_dim, height, width], device=concat_latent_image.device, dtype=concat_latent_image.dtype)
        
        # Ensure temporal dimension matches
        if concat_latent_image.shape[2] != temp_dim:
            # Resample latent to match expected temporal dimension
            print(f"Resampling latent from {concat_latent_image.shape[2]} to {temp_dim}")
            from torch.nn import functional as F
            concat_latent_image = F.interpolate(
                concat_latent_image,
                size=(temp_dim, height, width),
                mode="trilinear",
                align_corners=False
            )

        # Create mask based on FULL temporal length
        mask = torch.ones(
            (1, 1, temp_dim, height, width),
            device=concat_latent_image.device,
            dtype=concat_latent_image.dtype
        )
        mask[:, :, :1] = 0.0  # Mask all conditioning frames

        # Update conditioning
        positive = node_helpers.conditioning_set_values(positive, {
            "concat_latent_image": concat_latent_image,
            "concat_mask": mask
        })
        negative = node_helpers.conditioning_set_values(negative, {
            "concat_latent_image": concat_latent_image,
            "concat_mask": mask
        })

        return (positive, negative, {"samples": latent})
    