import os
import random
import folder_paths
import hashlib
import safetensors.torch

class LoadLatentFromAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "latent_path": ("STRING", {"default": ""}),
            }
        }

    CATEGORY = "latent"
    RETURN_TYPES = ("LATENT", "INT")
    FUNCTION = "load_latent"
    TITLE = "Load Latent (Absolute Path)"

    def load_latent(self, latent_path):
        # Check if path exists
        if not os.path.exists(latent_path):
            raise ValueError(f"Latent file not found at path: {latent_path}")

        latent = safetensors.torch.load_file(latent_path, device="cpu")
        multiplier = 1.0
        if "latent_format_version_0" not in latent:
            multiplier = 1.0 / 0.18215
        samples = {"samples": latent["latent_tensor"].float() * multiplier}
        return (samples, random.randint(0, 2**31 - 1))

    @classmethod
    def IS_CHANGED(s, latent_path):
        image_path = folder_paths.get_annotated_filepath(latent_path)
        m = hashlib.sha256()
        with open(image_path, "rb") as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, latent_path):
        if not folder_paths.exists_annotated_filepath(latent_path):
            return "Invalid latent file: {}".format(latent_path)
        return True
