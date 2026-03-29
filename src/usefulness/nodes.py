from .load_latent import LoadLatentFromOutput
from .load_latent_abs import LoadLatentFromAbs
from .save_latent_abs import SaveLatentToAbs
from .save_images_abs import SaveImagesToAbs
from .parse_json_array import ParseJSONArray
from .load_images_abs import LoadImagesFromAbs
from .save_string_abs import SaveStringToAbs
from .load_string_abs import LoadStringFromAbs
from .select_latent import LatentSelector
from .wan_latent_loader import WanLatentImageToVideo
from .wan_latent_loader_b import WanImageToVideoAlt
from .pad_latent import LatentPadder
from .concat_latent import ContatenatedLatent
from .color_mix import GradualColorMix

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "UFNLoadLatentFromOutput": LoadLatentFromOutput,
    "UFNLoadLatentFromAbsolutePath": LoadLatentFromAbs,
    "UFNLatentSelector": LatentSelector,
    "UFNLatentImageToVideo": WanLatentImageToVideo,
    "UFNLatentImageToVideoB": WanImageToVideoAlt,
    "UFNLatentPadder": LatentPadder,
    "UFNConcatLatent": ContatenatedLatent,
    "UFNGradualColorMix": GradualColorMix,
    "UFNSaveLatentToAbsolutePath": SaveLatentToAbs,
    "UFNSaveStringToAbsolutePath": SaveStringToAbs,
    "UFNLoadStringFromAbsolutePath": LoadStringFromAbs,
    "UFNSaveImagesToAbsolutePath": SaveImagesToAbs,
    "UFNParseJSONArray": ParseJSONArray,
    "UFNLoadImagesFromAbsolutePath": LoadImagesFromAbs
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "UFNLoadLatentFromOutput": "UFN Load Latent (Output)",
    "UFNLoadLatentFromAbsolutePath": "UFN Load Latent (Absolute Path)",
    "UFNLatentSelector": "UFN Latent Selector",
    "UFNLatentImageToVideo": "UFN Latent Image to Video",
    "UFNLatentImageToVideoB": "UFN Latent Image to Video (Alt)",
    "UFNLatentPadder": "UFN Latent Padder",
    "UFNConcatLatent": "UFN Concatenate Latent",
    "UFNGradualColorMix": "UFN Gradual Color Mix",
    "UFNSaveLatentToAbsolutePath": "UFN Save Latent (Absolute Path)",
    "UFNSaveStringToAbsolutePath": "UFN Save String (Absolute Path)",
    "UFNLoadStringFromAbsolutePath": "UFN Load String (Absolute Path)",
    "UFNSaveImagesToAbsolutePath": "UFN Save Images (Absolute Path)",
    "UFNParseJSONArray": "UFN Parse JSON Array",
    "UFNLoadImagesFromAbsolutePath": "UFN Load Images (Absolute Path)"
}
