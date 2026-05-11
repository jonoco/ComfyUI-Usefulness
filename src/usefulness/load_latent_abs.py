from pathlib import Path
import random
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
        path = Path(latent_path)
        if not path.exists():
            raise ValueError(f"Latent file not found at path: {path}")

        latent = safetensors.torch.load_file(path, device="cpu")
        multiplier = 1.0
        if "latent_format_version_0" not in latent:
            multiplier = 1.0 / 0.18215
        samples = {"samples": latent["latent_tensor"].float() * multiplier}

        # Include a random integer to force downstream nodes to refresh
        return (samples, random.randint(0, 2**31 - 1))

    @classmethod
    def IS_CHANGED(s, **kwargs):
        import time
        return str(time.time())
