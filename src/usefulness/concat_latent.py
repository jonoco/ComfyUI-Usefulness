import torch
from comfy.sd import VAE
from nodes import common_ksampler
import nodes
import torch.nn.functional as F

class ContatenatedLatent:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first_latent": ("LATENT",),
                "second_latent": ("LATENT",),
            },
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "concat_latent"
    CATEGORY = "Wan/latent"

    def concat_latent(self, first_latent, second_latent):
        first_samples = first_latent["samples"]
        fist_samples_length = (first_samples.shape[2] - 1) * 4 + 1
        print("first_samples shape:", first_samples.shape)
        print("fist_samples_length:", fist_samples_length)
            
        second_samples = second_latent["samples"]
        second_samples_length = (second_samples.shape[2] - 1) * 4 + 1
        print("second_samples shape:", second_samples.shape)
        print("second_samples_length:", second_samples_length)
        
        total_length = fist_samples_length + second_samples_length
        new_length = ((total_length - 1) // 4) + 1
        print("total_length:", total_length)
        print("new_length:", new_length)
        
        result = torch.cat([first_samples, second_samples], dim=2)
        
        print("Concatenated samples latent shape:", result.shape)
        
        return ({"samples": result},)
