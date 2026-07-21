import torch


class ContatenatedLatent:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "first_latent": ("LATENT",),
                "second_latent": ("LATENT",),
            },
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "concat_latent"
    CATEGORY = "Wan/latent"

    def concat_latent(self, first_latent, second_latent):
        first_samples = first_latent["samples"]
        fist_samples_length = (first_samples.shape[2] - 1) * 4 + 1

        second_samples = second_latent["samples"]
        second_samples_length = (second_samples.shape[2] - 1) * 4 + 1

        total_length = fist_samples_length + second_samples_length
        new_length = ((total_length - 1) // 4) + 1

        result = torch.cat([first_samples, second_samples], dim=2)
        print(
            f"first_samples shape: {first_samples.shape}\n"
            f"fist_samples_length: {fist_samples_length}\n"
            f"second_samples shape: {second_samples.shape}\n"
            f"second_samples_length: {second_samples_length}\n"
            f"total_length: {total_length}\n"
            f"new_length: {new_length}\n"
            f"result.shape: {result.shape}"
        )


        return ({"samples": result},)
