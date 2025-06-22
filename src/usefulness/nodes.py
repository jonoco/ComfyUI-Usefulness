from .model_switcher import ModelSwitcher
from .load_latent import LoadLatentFromOutput
from .load_latent_abs import LoadLatentFromAbs
from .select_latent import LatentSelector
from .wan_latent_loader import WanLatentImageToVideo
from .wan_latent_loader_b import WanImageToVideoAlt
from .pad_latent import LatentPadder
from .concat_latent import ContatenatedLatent

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "UFNModelSwitcher": ModelSwitcher,
    "UFNLoadLatentFromOutput": LoadLatentFromOutput,
    "UFNLoadLatentFromAbsolutePath": LoadLatentFromAbs,
    "UFNLatentSelector": LatentSelector,
    "UFNLatentImageToVideo": WanLatentImageToVideo,
    "UFNLatentImageToVideoB": WanImageToVideoAlt,
    "UFNLatentPadder": LatentPadder,
    "UFNConcatLatent": ContatenatedLatent,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "UFNModelSwitcher": "UFN Model Switcher",
    "UFNLoadLatentFromOutput": "UFN Load Latent (Output)",
    "UFNLoadLatentFromAbsolutePath": "UFN Load Latent (Absolute Path)",
    "UFNLatentSelector": "UFN Latent Selector",
    "UFNLatentImageToVideo": "UFN Latent Image to Video",
    "UFNLatentImageToVideoB": "UFN Latent Image to Video (Alt)",
    "UFNLatentPadder": "UFN Latent Padder",
    "UFNConcatLatent": "UFN Concatenate Latent",
}
