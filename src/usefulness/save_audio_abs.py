import json
import os

import scipy.io.wavfile

from ._date_wildcard import expand_date_wildcards


class SaveAudioToAbs:
    """
    A node that saves a batch of audio to an absolute path and returns a JSON string with the file paths and count.
    The returned JSON string has the following format:
    {
        "audio": ["path/to/audio_00000.wav", "path/to/audio_00001.wav", ...],
        "count": 10
    }
    """
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "audio": ("AUDIO",),
                "directory": ("STRING", {"default": ""}),
                "filename_prefix": ("STRING", {"default": "audio"}),
            }
        }

    CATEGORY = "audio"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("audio_json",)
    FUNCTION = "save_audio"
    TITLE = "Save Audio (Absolute Path)"
    OUTPUT_NODE = True

    def save_audio(self, audio, directory, filename_prefix):
        directory = expand_date_wildcards(directory)
        filename_prefix = expand_date_wildcards(filename_prefix)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        waveform = audio["waveform"]
        sample_rate = audio["sample_rate"]

        audio_paths = []
        for batch_number in range(waveform.shape[0]):
            filename = f"{filename_prefix}_{batch_number:05}.wav"
            filepath = os.path.join(directory, filename)

            audio_data = waveform[batch_number].cpu().numpy().T
            if audio_data.ndim == 1:
                audio_data = audio_data.reshape(-1, 1)

            scipy.io.wavfile.write(filepath, sample_rate, audio_data)
            audio_paths.append(filepath)

        result = {
            "audio": audio_paths,
            "count": len(audio_paths),
        }

        return (json.dumps(result),)
