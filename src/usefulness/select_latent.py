import torch
from comfy.sd import VAE
from nodes import common_ksampler

class LatentSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "start_index": ("INT", {"default": 0, "min": -999999, "max": 99999, "step": 4}),
                "end_index": ("INT", {"default": 0, "min": -999999, "max": 99999, "step": 4}),
                "use_end_index": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT")
    RETURN_NAMES = ("latent", "selected_count")
    FUNCTION = "select_latent"
    CATEGORY = "Wan/latent"

    def select_latent(self, latent, start_index, end_index, use_end_index):
        samples = latent["samples"]
        length = (samples.shape[2] - 1) * 4 + 1
        
        if start_index >= length:
            raise ValueError(f"Start index {start_index} is out of bounds for latent with length {length}")
        # if end_index > length:
        #     raise ValueError(f"End index {end_index} is out of bounds for latent with length {length}")
        # if start_index >= end_index:
        #     raise ValueError(f"Start index {start_index} must be less than end index {end_index}")
        # if end_index % 4 != 0:
        #     raise ValueError(f"End index {end_index} must be a multiple of 4")
        
        start_sample_index = int(start_index / 4)

        # if start_sample_index == end_sample_index:
        #     raise ValueError(f"Start and end sample indices {start_sample_index} must be different")
        if use_end_index:
            if end_index < start_index:
                raise ValueError(f"End index {end_index} must be greater than or equal to start index {start_index}")
            end_sample_index = int(end_index / 4) + 1
        else:
            end_sample_index = samples.shape[2]

        selected = samples[:, :, start_sample_index:end_sample_index, :, :]
        
        selected_count = selected.shape[2] * 4 - 3  # Convert back to original length
        print("Selected latent shape:", selected.shape)
        
        return ({"samples": selected}, selected_count)
