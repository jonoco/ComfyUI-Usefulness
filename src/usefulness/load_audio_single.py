import hashlib
import os

import scipy.io.wavfile
import torch


class LoadSingleAudioFromAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "path": ("STRING",),
            }
        }

    CATEGORY = "audio"
    RETURN_TYPES = ("AUDIO", "FLOAT")
    RETURN_NAMES = ("audio", "duration")
    FUNCTION = "load_audio"
    TITLE = "Load Single Audio (Absolute Path)"

    def load_audio(self, path):
        if not isinstance(path, str):
            raise ValueError(f"Path must be a string, got {type(path).__name__}")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        sr, audio_data = scipy.io.wavfile.read(path)

        if audio_data.dtype == "int16":
            audio_data = audio_data.astype("float32") / 32768.0
        elif audio_data.dtype == "int32":
            audio_data = audio_data.astype("float32") / 2147483648.0
        elif audio_data.dtype == "uint8":
            audio_data = (audio_data.astype("float32") - 128) / 128.0

        waveform = torch.from_numpy(audio_data).float()
        if waveform.ndim == 1:
            waveform = waveform.unsqueeze(0)
        else:
            waveform = waveform.T

        num_frames = waveform.shape[-1]
        duration = float(num_frames / sr)

        batch = waveform.unsqueeze(0)

        return ({"waveform": batch, "sample_rate": sr}, duration)

    @classmethod
    def IS_CHANGED(s, path):
        m = hashlib.sha256()
        return m.digest().hex()
