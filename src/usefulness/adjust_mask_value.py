import torch


class AdjustMaskValue:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("MASK",),
                "upper_limit": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                "lower_limit": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("MASK",)
    FUNCTION = "adjust"
    CATEGORY = "mask"
    TITLE = "Adjust Mask Value"

    def adjust(self, mask, upper_limit, lower_limit):
        mask = torch.clamp(mask, 0.0, 1.0)
        adjusted = mask * (upper_limit - lower_limit) + lower_limit
        return (adjusted,)
