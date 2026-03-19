import torch


class LatentSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "dim": ("INT", {"default": 2, "min": 0, "max": 5, "step": 1}),
                "start_index": ("INT", {"default": 0, "min": -999999, "max": 99999, "step": 1}),
                "end_index": ("INT", {"default": 0, "min": -999999, "max": 99999, "step": 1}),
                "use_end_index": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("LATENT", "INT")
    RETURN_NAMES = ("latent", "selected_count")
    FUNCTION = "select_latent"
    CATEGORY = "latent"

    def select_latent(self, latent, dim, start_index, end_index, use_end_index):
        samples = latent["samples"]
        if dim >= len(samples.shape):
            raise ValueError(f"Dimension {dim} is out of bounds for latent with shape {samples.shape}")
        dim_size = samples.shape[dim]

        # Handle negative indices (Python-style indexing from end)
        if start_index < 0:
            start_index = dim_size + start_index
        if end_index < 0:
            end_index = dim_size + end_index

        # Clamp indices to valid range
        start_index = max(0, min(start_index, dim_size))
        end_index = max(0, min(end_index, dim_size))

        if start_index >= dim_size:
            raise ValueError(f"Start index {start_index} is out of bounds for dimension with size {dim_size}")

        if use_end_index:
            if end_index < start_index:
                raise ValueError(f"End index {end_index} must be greater than or equal to start index {start_index}")
            end_sample_index = end_index
        else:
            end_sample_index = dim_size

        selected = samples.index_select(dim, torch.arange(start_index, end_sample_index))

        selected_count = selected.shape[dim]
        print("Selected latent shape:", selected.shape)

        return ({"samples": selected}, selected_count)
