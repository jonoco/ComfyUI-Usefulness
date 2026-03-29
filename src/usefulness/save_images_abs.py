import json
import os

import numpy as np
from PIL import Image


class SaveImagesToAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "directory": ("STRING", {"default": ""}),
                "filename_prefix": ("STRING", {"default": "image"}),
            }
        }

    CATEGORY = "image"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("images_json",)
    FUNCTION = "save_images"
    TITLE = "Save Images (Absolute Path)"
    OUTPUT_NODE = True

    def save_images(self, images, directory, filename_prefix):
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        image_paths = []
        for batch_number, image in enumerate(images):
            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            filename = f"{filename_prefix}_{batch_number:05}.png"
            filepath = os.path.join(directory, filename)
            img.save(filepath)
            image_paths.append(filepath)

        result = {
            "images": image_paths,
            "count": len(image_paths),
        }

        return (json.dumps(result),)
