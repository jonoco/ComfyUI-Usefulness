import nodes
import torch.nn.functional as F


class LatentPadder:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "total_length": ("INT", {"default": 81, "min": 1, "max": nodes.MAX_RESOLUTION, "step": 4}),
            },
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "pad_latent"
    CATEGORY = "Wan/latent"

    def pad_latent(self, latent, total_length):
        samples = latent["samples"]
        samples_length = (samples.shape[2] - 1) * 4 + 1

        new_frames = total_length - samples_length
        if new_frames < 0:
            raise ValueError(f"Total length {total_length} is less than the current length {samples_length}")
        if new_frames % 4 != 0:
            raise ValueError(f"Total length {total_length} must be a multiple of 4")

        new_length = ((new_frames - 1) // 4) + 1

        padded_tensor = F.pad(samples, (0, 0, 0, 0, 0, new_length, 0, 0, 0, 0))

        # padded_tensor = torch.zeros(samples.size(0), samples.size(1),  ((total_length - 1) // 4) + 1, samples.size(3), samples.size(4),
        #                   device=samples.device, dtype=samples.dtype)
        # padded_tensor[:, :, :samples.size(2), :, :] = samples

        print("Padded samples latent shape:", padded_tensor.shape)

        return ({"samples": padded_tensor},)
