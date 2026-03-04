import torch
import numpy as np
from PIL import Image

class GradualColorMix:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images_a": ("IMAGE",),
                "images_b": ("IMAGE",),
                "blend_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "blend_images"
    CATEGORY = "image/postprocessing"

    def blend_images(self, images_a, images_b, blend_strength):
        # Ensure both batches have the same number of images
        batch_size = images_a.shape[0]
        if images_b.shape[0] != batch_size:
            # If one batch is smaller, repeat the last image to match sizes
            if images_b.shape[0] < batch_size:
                last_img = images_b[-1].unsqueeze(0)
                repeat_count = batch_size - images_b.shape[0]
                images_b = torch.cat([images_b, last_img.repeat(repeat_count, 1, 1, 1)], dim=0)
            else:
                images_b = images_b[:batch_size]
        
        results = []
        
        for i in range(batch_size):
            # Calculate the blend ratio for this image in the batch
            ratio = (i / (batch_size - 1)) * blend_strength if batch_size > 1 else blend_strength
            
            # Blend the two images
            blended = images_a[i] * (1 - ratio) + images_b[i] * ratio
            results.append(blended.unsqueeze(0))
        
        return (torch.cat(results, dim=0),)
