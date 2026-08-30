import torch


class NormalizeMaskValue:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
            }
        }

    RETURN_TYPES = ("MASK",)
    FUNCTION = "normalize"
    CATEGORY = "mask"
    TITLE = "Normalize Mask Value"

    def normalize(self, mask):
        mask = torch.clamp(mask, min=0.0)
        max_value = float(mask.max().item())

        if max_value <= 0.0:
            return (torch.zeros_like(mask),)

        return (mask / max_value,)
