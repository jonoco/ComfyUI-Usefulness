import torch
from nodes import common_ksampler
from nodes import node_helpers
import nodes
import comfy.model_management

class WanLatentImageToVideo:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"positive": ("CONDITIONING", ),
                             "negative": ("CONDITIONING", ),
                             "length": ("INT", {"default": 81, "min": 1, "max": nodes.MAX_RESOLUTION, "step": 4}),
                             "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
                             "start_latent": ("LATENT", ),
                },}

    RETURN_TYPES = ("CONDITIONING", "CONDITIONING", "LATENT")
    RETURN_NAMES = ("positive", "negative", "latent", "width", "height")
    TITLE = "Wan Latent Image to Video"
    FUNCTION = "encode"

    CATEGORY = "conditioning/video_models"

    def encode(self, positive, negative, length, batch_size, start_latent):
        samples = start_latent["samples"]
        num_frames = samples.shape[2]  # Shape: [batch, channels, frames, H, W]
        width = samples.shape[4]
        height = samples.shape[3]
        latent = torch.zeros([batch_size, 16, ((length - 1) // 4) + 1, height, width], device=comfy.model_management.intermediate_device())
        
        # concat_latent = torch.ones([batch_size, 16, ((length - 1) // 4) + 1, height, width], device=comfy.model_management.intermediate_device())
        # concat_latent = comfy.latent_formats.Wan21().process_out(concat_latent)
        # concat_latent = concat_latent.repeat(1, 2, 1, 1, 1)
        # concat_latent[:,16:,:samples.shape[2]] = samples[:,:,:concat_latent.shape[2]]
       
        # mask = torch.ones_like(samples)
        mask = torch.ones((1, 1, latent.shape[2], height, width), device=samples.device, dtype=samples.dtype)
        # mask[:, :, :((samples.shape[2] - 1) // 4) + 1] = 0.0
        mask[:, :, :num_frames] = 0.0
        
        print("mask shape:", mask.shape)
        print("latent shape:", latent.shape)
        print("samples shape:", samples.shape)

        # positive = node_helpers.conditioning_set_values(positive, {"concat_latent_image": concat_latent, "concat_mask": mask})
        # negative = node_helpers.conditioning_set_values(negative, {"concat_latent_image": concat_latent, "concat_mask": mask})
        positive = node_helpers.conditioning_set_values(positive, {"concat_latent_image": samples, "concat_mask": mask})
        negative = node_helpers.conditioning_set_values(negative, {"concat_latent_image": samples, "concat_mask": mask})

        out_latent = {}
        out_latent["samples"] = latent
        return (positive, negative, out_latent, width, height)
