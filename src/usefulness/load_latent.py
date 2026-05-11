import os
import folder_paths
import hashlib

import torch
import safetensors.torch
from PIL import Image
from functools import lru_cache
import numpy as np

import node_helpers


class LoadLatentFromOutput:
    @classmethod
    @lru_cache(maxsize=None)
    def scan_latent_files(cls):
        input_dir = folder_paths.get_output_directory()
        files = []
        for root, _, walk_files in os.walk(input_dir):
            for file in walk_files:
                if file.endswith(".latent"):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, input_dir)
                    files.append(rel_path)
        return sorted(files)

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"latent": (cls.scan_latent_files(),)}, "optional": {"refresh": ("BOOLEAN", {"default": False})}}

    CATEGORY = "_for_testing"
    RETURN_TYPES = ("LATENT", "IMAGE")
    RETURN_NAMES = ("latent", "preview")
    FUNCTION = "load"

    def load(self, latent, refresh=False):
        # Load latent
        input_dir = folder_paths.get_output_directory()

        latent_path = os.path.join(input_dir, latent)
        latent_data = safetensors.torch.load_file(latent_path, device="cpu")
        multiplier = 1.0 / 0.18215 if "latent_format_version_0" not in latent_data else 1.0
        samples = {"samples": latent_data["latent_tensor"].float() * multiplier}

        # Find and load preview image
        preview_dir = os.path.dirname(latent_path)
        base_name = os.path.splitext(os.path.basename(latent))[0]

        # Split the base name from the filename increment eg. file_0001.png
        if "_" in base_name:
            base_name = base_name.split("_")[0]

        # Find the image file that begins with the base name
        preview_files = [f for f in os.listdir(preview_dir) if f.startswith(base_name) and f.endswith((".png", ".jpg", ".jpeg"))]
        if not preview_files:
            print(f"No preview image found for {latent}.")
            return (samples, None)

        # Use the first matching preview file
        preview_file = preview_files[0]
        preview_path = os.path.join(preview_dir, preview_file)

        # Check if the preview image exists
        if not os.path.exists(preview_path):
            print(f"Preview image not found at {preview_path}.")
            return (samples, None)

        preview_tensor = None
        if os.path.exists(preview_path):
            print(f"Loading preview image from {preview_path}")
            node_helpers.pillow(Image.open, preview_path)

            pil_image = Image.open(preview_path)
            preview_tensor = pil_image.convert("RGB")
            preview_tensor = np.array(preview_tensor).astype(np.float32) / 255.0
            preview_tensor = torch.from_numpy(preview_tensor)[None,]

        return (samples, preview_tensor)

    @classmethod
    def IS_CHANGED(s, latent, refresh=False):
        if refresh:
            s.scan_latent_files.cache_clear()
            return float("nan")

        file_path = folder_paths.get_annotated_filepath(latent)
        m = hashlib.sha256()
        with open(file_path, "rb") as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, latent):
        input_dir = folder_paths.get_output_directory()
        latent_path = os.path.join(input_dir, latent)

        if not os.path.exists(latent_path):
            return "Invalid latent file: {}".format(latent_path)
        return True
