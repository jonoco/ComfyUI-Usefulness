import json
import os

import numpy as np
import torch
from PIL import Image


class LoadImagesFromAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "array_json": ("STRING",),
            }
        }

    CATEGORY = "image"
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load_images"
    TITLE = "Load Images (Absolute Path)"

    def load_images(self, array_json):
        paths = json.loads(array_json)

        if not isinstance(paths, list):
            raise ValueError("Input must be a JSON array of file paths")

        images = []
        for path in paths:
            if not isinstance(path, str):
                raise ValueError(f"Array values must be strings, got {type(path).__name__}")
            if not os.path.exists(path):
                raise FileNotFoundError(f"File not found: {path}")

            img = Image.open(path)
            img = img.convert("RGB")
            img_array = np.array(img).astype(np.float32) / 255.0
            images.append(torch.from_numpy(img_array))

        batch = torch.stack(images)
        return (batch,)

    @classmethod
    def IS_CHANGED(s, **kwargs):
        import time
        return str(time.time())
