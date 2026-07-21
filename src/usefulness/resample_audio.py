import torch
import torch.nn.functional as F


class ResampleAudio:
    """Resample an AUDIO tensor to a target sample rate using linear interpolation."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio": ("AUDIO",),
                "target_sample_rate": (
                    "INT",
                    {
                        "default": 44100,
                        "min": 1,
                        "max": 384000,
                        "step": 1,
                    },
                ),
            }
        }

    CATEGORY = "audio"
    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("resampled_audio",)
    FUNCTION = "resample_audio"
    TITLE = "Resample Audio"

    def resample_audio(self, audio, target_sample_rate):
        waveform = audio["waveform"]
        source_sample_rate = int(audio["sample_rate"])
        target_sample_rate = int(target_sample_rate)

        if target_sample_rate <= 0:
            raise ValueError(f"target_sample_rate must be > 0, got {target_sample_rate}")

        if source_sample_rate <= 0:
            raise ValueError(f"audio sample_rate must be > 0, got {source_sample_rate}")

        if source_sample_rate == target_sample_rate:
            return ({"waveform": waveform, "sample_rate": target_sample_rate},)

        if waveform.ndim != 3:
            raise ValueError(
                "Expected audio waveform shape [batch, channels, samples], "
                f"got shape {tuple(waveform.shape)}"
            )

        source_samples = waveform.shape[-1]
        target_samples = max(1, int(round(source_samples * target_sample_rate / source_sample_rate)))

        resampled = F.interpolate(
            waveform,
            size=target_samples,
            mode="linear",
            align_corners=False,
        )

        return ({"waveform": resampled, "sample_rate": target_sample_rate},)
