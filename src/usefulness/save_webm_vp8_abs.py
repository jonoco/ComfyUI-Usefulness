import os
import shutil
import subprocess
import tempfile

import numpy as np
import scipy.io.wavfile
from PIL import Image

from ._date_wildcard import expand_date_wildcards


class SaveWebMVP8ToAbs:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "audio": ("AUDIO",),
                "directory": ("STRING", {"default": ""}),
                "filename_prefix": ("STRING", {"default": "video"}),
                "frame_rate": ("FLOAT", {"default": 24.0, "min": 1.0, "max": 240.0, "step": 0.01}),
                "quality": ("INT", {"default": 20, "min": 4, "max": 63, "step": 1}),
            },
            "optional": {
                "alpha": ("MASK",),
            },
        }

    CATEGORY = "image"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("video_path",)
    FUNCTION = "save_video"
    TITLE = "Save VP8 WebM with Audio (Absolute Path)"
    OUTPUT_NODE = True

    def save_video(self, images, audio, directory, filename_prefix, frame_rate, quality, alpha=None):
        ffmpeg_path = shutil.which("ffmpeg")
        if ffmpeg_path is None:
            raise RuntimeError("ffmpeg was not found in PATH")

        directory = expand_date_wildcards(directory)
        filename_prefix = expand_date_wildcards(filename_prefix)
        os.makedirs(directory, exist_ok=True)

        video_path = os.path.join(directory, f"{filename_prefix}.webm")
        waveform = audio["waveform"]
        sample_rate = audio["sample_rate"]

        if waveform.shape[0] != 1:
            raise ValueError("Audio input must contain exactly one track")

        alpha_frames = self._prepare_alpha(alpha, images.shape[0], images.shape[1], images.shape[2])

        with tempfile.TemporaryDirectory(prefix="ufn_webm_") as temp_dir:
            frame_pattern = os.path.join(temp_dir, "frame_%06d.png")
            audio_path = os.path.join(temp_dir, "audio.wav")

            self._write_frames(images, frame_pattern, alpha_frames)
            self._write_audio(audio_path, waveform, sample_rate)

            command = [
                ffmpeg_path,
                "-y",
                "-framerate",
                str(frame_rate),
                "-start_number",
                "0",
                "-i",
                frame_pattern,
                "-i",
                audio_path,
                "-c:v",
                "libvpx",
                "-pix_fmt",
                "yuva420p",
                "-auto-alt-ref",
                "0",
                "-crf",
                str(quality),
                "-b:v",
                "0",
                "-c:a",
                "libvorbis",
                "-shortest",
                video_path,
            ]

            result = subprocess.run(command, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                raise RuntimeError(f"ffmpeg failed with exit code {result.returncode}: {result.stderr.strip()}")

        return (video_path,)

    def _prepare_alpha(self, alpha, frame_count, height, width):
        if alpha is None:
            return None

        alpha_array = alpha.cpu().numpy()
        if alpha_array.ndim == 2:
            alpha_array = np.expand_dims(alpha_array, axis=0)

        if alpha_array.ndim != 3:
            raise ValueError("Alpha mask must have shape [frames, height, width] or [height, width]")

        if alpha_array.shape[0] not in (1, frame_count):
            raise ValueError("Alpha mask batch must have either one frame or match the image batch size")

        if alpha_array.shape[1:] != (height, width):
            raise ValueError("Alpha mask dimensions must match the input image dimensions")

        return np.clip(alpha_array, 0.0, 1.0)

    def _write_frames(self, images, frame_pattern, alpha_frames):
        for frame_index, image in enumerate(images):
            rgb = np.clip(255.0 * image.cpu().numpy(), 0, 255).astype(np.uint8)
            if rgb.ndim != 3 or rgb.shape[2] != 3:
                raise ValueError("Image input must contain RGB frames")

            if alpha_frames is None:
                alpha_channel = np.full((rgb.shape[0], rgb.shape[1], 1), 255, dtype=np.uint8)
            else:
                alpha_index = 0 if alpha_frames.shape[0] == 1 else frame_index
                alpha_channel = np.clip(255.0 * alpha_frames[alpha_index], 0, 255).astype(np.uint8)[..., None]

            rgba = np.concatenate((rgb, alpha_channel), axis=2)
            output_path = frame_pattern % frame_index
            Image.fromarray(rgba, mode="RGBA").save(output_path)

    def _write_audio(self, audio_path, waveform, sample_rate):
        audio_data = waveform[0].cpu().numpy().T
        if audio_data.ndim == 1:
            audio_data = audio_data.reshape(-1, 1)

        scipy.io.wavfile.write(audio_path, sample_rate, audio_data)
