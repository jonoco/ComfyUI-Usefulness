from .load_latent import LoadLatentFromOutput
from .load_latent_abs import LoadLatentFromAbs
from .save_latent_abs import SaveLatentToAbs
from .save_images_abs import SaveImagesToAbs
from .parse_json_array import ParseJSONArray
from .concat_json_array import ConcatJSONArray
from .array_to_json_dict import ArrayToJSONDict
from .slice_json_array import SliceJSONArray
from .get_string_from_array import GetStringFromJSONArray
from .get_int_from_array import GetIntFromJSONArray
from .get_float_from_array import GetFloatFromJSONArray
from .load_images_abs import LoadImagesFromAbs
from .save_audio_abs import SaveAudioToAbs
from .load_audio_abs import LoadAudioFromAbs
from .load_audio_single import LoadSingleAudioFromAbs
from .merge_audio_with_transition import MergeAudioWithTransition
from .save_string_abs import SaveStringToAbs
from .load_string_abs import LoadStringFromAbs
from .select_latent import LatentSelector
from .wan_latent_loader import WanLatentImageToVideo
from .wan_latent_loader_b import WanImageToVideoAlt
from .pad_latent import LatentPadder
from .concat_latent import ContatenatedLatent
from .color_mix import GradualColorMix
from .solid_color import SolidColorImage
from .grayscale_color import GrayscaleColorImage
from .adjust_mask_value import AdjustMaskValue

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
    "UFNSolidColorImage": SolidColorImage,
    "UFNGrayscaleColorImage": GrayscaleColorImage,
    "UFNAdjustMaskValue": AdjustMaskValue,
    "UFNSaveLatentToAbsolutePath": SaveLatentToAbs,
    "UFNSaveStringToAbsolutePath": SaveStringToAbs,
    "UFNLoadStringFromAbsolutePath": LoadStringFromAbs,
    "UFNSaveImagesToAbsolutePath": SaveImagesToAbs,
    "UFNParseJSONArray": ParseJSONArray,
    "UFNLoadImagesFromAbsolutePath": LoadImagesFromAbs,
    "UFNSaveAudioToAbsolutePath": SaveAudioToAbs,
    "UFNLoadAudioFromAbsolutePath": LoadAudioFromAbs,
    "UFNLoadSingleAudioFromAbsolutePath": LoadSingleAudioFromAbs,
    "UFNMergeAudioWithTransition": MergeAudioWithTransition,
    "UFNConcatJSONArray": ConcatJSONArray,
    "UFNArrayToJSONDict": ArrayToJSONDict,
    "UFNSliceJSONArray": SliceJSONArray,
    "UFNGetStringFromJSONArray": GetStringFromJSONArray,
    "UFNGetIntFromJSONArray": GetIntFromJSONArray,
    "UFNGetFloatFromJSONArray": GetFloatFromJSONArray
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
    "UFNSolidColorImage": "UFN Solid Color Image",
    "UFNGrayscaleColorImage": "UFN Grayscale Color Image",
    "UFNAdjustMaskValue": "UFN Adjust Mask Value",
    "UFNSaveLatentToAbsolutePath": "UFN Save Latent (Absolute Path)",
    "UFNSaveStringToAbsolutePath": "UFN Save String (Absolute Path)",
    "UFNLoadStringFromAbsolutePath": "UFN Load String (Absolute Path)",
    "UFNSaveImagesToAbsolutePath": "UFN Save Images (Absolute Path)",
    "UFNParseJSONArray": "UFN Parse JSON Array",
    "UFNLoadImagesFromAbsolutePath": "UFN Load Images (Absolute Path)",
    "UFNSaveAudioToAbsolutePath": "UFN Save Audio (Absolute Path)",
    "UFNLoadAudioFromAbsolutePath": "UFN Load Audio (Absolute Path)",
    "UFNLoadSingleAudioFromAbsolutePath": "UFN Load Single Audio (Absolute Path)",
    "UFNMergeAudioWithTransition": "UFN Merge Audio with Transition",
    "UFNConcatJSONArray": "UFN Concatenate JSON Arrays",
    "UFNArrayToJSONDict": "UFN Array to JSON Dict",
    "UFNSliceJSONArray": "UFN Slice JSON Array",
    "UFNGetStringFromJSONArray": "UFN Get String from JSON Array",
    "UFNGetIntFromJSONArray": "UFN Get Int from JSON Array",
    "UFNGetFloatFromJSONArray": "UFN Get Float from JSON Array"
}
