import torch
import numpy as np


class MergeAudioWithTransition:
    """
    Merges two audio tracks with a configurable transition.

    - transition_start: Position in track A where track B begins (in seconds).
      Negative values are relative to the end of track A.
    - transition_duration: Length of the overlap in seconds.
      0 means concatenation with no overlap.
    - transition_method: How to blend the tracks during overlap.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio_a": ("AUDIO",),
                "audio_b": ("AUDIO",),
                "transition_start": (
                    "FLOAT",
                    {
                        "default": 0.0,
                        "min": -3600.0,
                        "max": 3600.0,
                        "step": 0.01,
                    },
                ),
                "transition_duration": (
                    "FLOAT",
                    {
                        "default": 0.0,
                        "min": 0.0,
                        "max": 60.0,
                        "step": 0.01,
                    },
                ),
                "transition_method": (
                    ["concat", "linear_crossfade", "equal_power_crossfade", "fade_in_fade_out"],
                    {"default": "linear_crossfade"},
                ),
            }
        }

    CATEGORY = "audio"
    RETURN_TYPES = ("AUDIO",)
    RETURN_NAMES = ("merged_audio",)
    FUNCTION = "merge_audio"
    TITLE = "Merge Audio with Transition"

    def merge_audio(self, audio_a, audio_b, transition_start, transition_duration, transition_method):
        """
        Merge two audio tracks with transition.

        Args:
            audio_a: First audio dict with 'waveform' and 'sample_rate'
            audio_b: Second audio dict with 'waveform' and 'sample_rate'
            transition_start: Start position in audio_a (in seconds, negative for end-relative)
            transition_duration: Duration of overlap (in seconds)
            transition_method: Method for blending ('concat', 'linear_crossfade', etc.)

        Returns:
            Merged audio dict
        """
        waveform_a = audio_a["waveform"]
        sr_a = audio_a["sample_rate"]

        waveform_b = audio_b["waveform"]
        sr_b = audio_b["sample_rate"]

        # Validate sample rates match
        if sr_a != sr_b:
            raise ValueError(f"Sample rates must match: {sr_a} vs {sr_b}")

        sr = sr_a

        # Handle batch dimension - work with first batch item
        if waveform_a.shape[0] > 1 or waveform_b.shape[0] > 1:
            raise ValueError("Only single-batch audio is supported")

        # Remove batch dimension: [1, channels, samples] -> [channels, samples]
        waveform_a = waveform_a.squeeze(0)
        waveform_b = waveform_b.squeeze(0)

        # Ensure mono or stereo
        if waveform_a.ndim == 1:
            waveform_a = waveform_a.unsqueeze(0)
        if waveform_b.ndim == 1:
            waveform_b = waveform_b.unsqueeze(0)

        channels_a = waveform_a.shape[0]
        channels_b = waveform_b.shape[0]

        # Match channel count
        if channels_a != channels_b:
            if channels_a == 1 and channels_b > 1:
                waveform_a = waveform_a.repeat(channels_b, 1)
                channels = channels_b
            elif channels_b == 1 and channels_a > 1:
                waveform_b = waveform_b.repeat(channels_a, 1)
                channels = channels_a
            else:
                raise ValueError(f"Incompatible channel counts: {channels_a} vs {channels_b}")
        else:
            channels = channels_a

        # Convert times from seconds to samples
        transition_samples = int(transition_duration * sr)
        transition_start_samples = int(transition_start * sr)

        # Calculate actual start position (handle negative indexing)
        length_a = waveform_a.shape[-1]
        if transition_start_samples < 0:
            start_pos = max(0, length_a + transition_start_samples)
        else:
            start_pos = min(transition_start_samples, length_a)

        # Build the output
        if transition_samples == 0:
            # Simple concatenation
            merged = torch.cat([waveform_a, waveform_b], dim=-1)
        else:
            # Calculate regions
            pre_transition_a = waveform_a[:, :start_pos]

            # Region where we need audio_b content
            transition_length = min(transition_samples, length_a - start_pos, waveform_b.shape[-1])

            # Extract the transition portion
            a_transition = waveform_a[:, start_pos : start_pos + transition_length]
            b_transition = waveform_b[:, :transition_length]

            # Create blending envelope
            blend = self._create_blend(transition_length, transition_method)
            blend_a = 1.0 - blend

            # Apply blend
            merged_transition = a_transition * blend_a + b_transition * blend

            # Post-transition audio_b
            b_remaining = waveform_b[:, transition_length:]

            # Post-transition audio_a (if any)
            a_remaining = waveform_a[:, start_pos + transition_length :]

            # Concatenate all parts
            merged = torch.cat([pre_transition_a, merged_transition, b_remaining, a_remaining], dim=-1)

        # Add batch dimension back
        merged = merged.unsqueeze(0)

        return ({"waveform": merged, "sample_rate": sr},)

    def _create_blend(self, length, method):
        """Create a blending envelope from 0 to 1 over the given length."""
        if method == "linear_crossfade":
            blend = torch.linspace(0, 1, length)
        elif method == "equal_power_crossfade":
            t = torch.linspace(0, 1, length)
            blend = torch.sin(t * np.pi / 2) ** 2
        elif method == "fade_in_fade_out":
            # Smooth sigmoidal fade
            t = torch.linspace(-4, 4, length)
            blend = 1.0 / (1.0 + torch.exp(-t))
        elif method == "concat":
            blend = torch.ones(length)
        else:
            raise ValueError(f"Unknown transition method: {method}")

        return blend.to(torch.float32)
