# Usefulness

Usefulness is a ComfyUI custom node pack with utility nodes for JSON, strings, masks, images, audio, and latents.

## Install

Clone this repository into your ComfyUI `custom_nodes` directory:

```bash
git clone https://github.com/jonoco/usefulness.git
```

If you are using ComfyUI Manager, install it from the manager.

## Requirements

This repository does not declare any extra package-specific dependencies.
The nodes expect the normal ComfyUI Python environment, which provides the runtime stack used here, including `torch`, `numpy`, `scipy`, `Pillow`, and `safetensors`.
The VP8 WebM export node also requires `ffmpeg` to be installed and available on `PATH`.

## Included Nodes

- JSON helpers: add, concat, parse, slice, and extract values from JSON dictionaries and arrays
- String helpers: load, save, and extract strings
- Mask helpers: normalize and adjust mask values
- Image helpers: grayscale conversion, solid color generation, image loading, and image saving
- Video helpers: VP8 WebM export with audio and optional alpha mask support through `ffmpeg`
- Audio helpers: load, save, resample, and transition mixing
- Latent helpers: load, save, concatenate, and select latents

## Layout

- `__init__.py` exposes the ComfyUI node mappings at the repository root.
- `src/usefulness/nodes.py` collects the node classes and display names.
- Individual node implementations live in `src/usefulness/*.py`.

## Notes

- There is no `web/` frontend for this pack.
- This repository is intended to be loaded as a ComfyUI custom node directory, not as a standalone application.
