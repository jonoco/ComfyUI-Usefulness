import torch


class GrayscaleColorImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 1, "max": 8192, "step": 1}),
                "height": ("INT", {"default": 512, "min": 1, "max": 8192, "step": 1}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096, "step": 1}),
                "value": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate"
    CATEGORY = "image/generate"
    TITLE = "Grayscale Color"

    def generate(self, width, height, batch_size, value):
        gray = torch.tensor([value, value, value], dtype=torch.float32)
        image = gray.view(1, 1, 1, 3).expand(batch_size, height, width, 3).clone()
        return (image,)
