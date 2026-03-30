import json
import os

import scipy.io.wavfile
import torch


class LoadAudioFromAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "array_json": ("STRING",),
            }
        }

    CATEGORY = "audio"
    RETURN_TYPES = ("AUDIO",)
    FUNCTION = "load_audio"
    TITLE = "Load Audio (Absolute Path)"

    def load_audio(self, array_json):
        paths = json.loads(array_json)

        if not isinstance(paths, list):
            raise ValueError("Input must be a JSON array of file paths")

        waveforms = []
        sample_rate = None

        for path in paths:
            if not isinstance(path, str):
                raise ValueError(f"Array values must be strings, got {type(path).__name__}")
            if not os.path.exists(path):
                raise FileNotFoundError(f"File not found: {path}")

            sr, audio_data = scipy.io.wavfile.read(path)

            if sample_rate is None:
                sample_rate = sr
            elif sr != sample_rate:
                raise ValueError(f"Sample rate mismatch: expected {sample_rate}, got {sr} for {path}")

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

            waveforms.append(waveform)

        batch = torch.stack(waveforms)

        return ({"waveform": batch, "sample_rate": sample_rate},)
