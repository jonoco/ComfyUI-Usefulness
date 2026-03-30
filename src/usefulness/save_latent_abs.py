import os

import safetensors.torch
import torch

from ._date_wildcard import expand_date_wildcards


class SaveLatentToAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "samples": ("LATENT",),
                "latent_path": ("STRING", {"default": ""}),
            }
        }

    CATEGORY = "latent"
    RETURN_TYPES = ()
    FUNCTION = "save_latent"
    TITLE = "Save Latent (Absolute Path)"
    OUTPUT_NODE = True

    def save_latent(self, samples, latent_path):
        latent_path = expand_date_wildcards(latent_path)
        # Ensure directory exists
        directory = os.path.dirname(latent_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Prepare tensors for saving
        latent_tensor = samples["samples"].contiguous()
        tensors = {
            "latent_tensor": latent_tensor,
            "latent_format_version_0": torch.tensor([]),
        }

        # Save using safetensors
        safetensors.torch.save_file(tensors, latent_path)

        return {}
