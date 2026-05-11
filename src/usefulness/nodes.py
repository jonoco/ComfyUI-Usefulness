from .adjust_mask_value import AdjustMaskValue
from .array_to_json_dict import ArrayToJSONDict
from .color_mix import GradualColorMix
from .concat_json_array import ConcatJSONArray
from .concat_latent import ContatenatedLatent
from .get_float_from_array import GetFloatFromJSONArray
from .get_int_from_array import GetIntFromJSONArray
from .get_string_from_array import GetStringFromJSONArray
from .grayscale_color import GrayscaleColorImage
from .load_audio_abs import LoadAudioFromAbs
from .load_audio_single import LoadSingleAudioFromAbs
from .load_images_abs import LoadImagesFromAbs
from .load_latent import LoadLatentFromOutput
from .load_latent_abs import LoadLatentFromAbs
from .load_string_abs import LoadStringFromAbs
from .merge_audio_with_transition import MergeAudioWithTransition
from .pad_latent import LatentPadder
from .parse_json_array import ParseJSONArray
from .save_audio_abs import SaveAudioToAbs
from .save_images_abs import SaveImagesToAbs
from .save_latent_abs import SaveLatentToAbs
from .save_string_abs import SaveStringToAbs
from .select_latent import LatentSelector
from .slice_json_array import SliceJSONArray
from .solid_color import SolidColorImage
from .wan_latent_loader import WanLatentImageToVideo
from .wan_latent_loader_b import WanImageToVideoAlt

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "UFNAdjustMaskValue": AdjustMaskValue,
    "UFNArrayToJSONDict": ArrayToJSONDict,
    "UFNConcatJSONArray": ConcatJSONArray,
    "UFNConcatLatent": ContatenatedLatent,
    "UFNGetFloatFromJSONArray": GetFloatFromJSONArray,
    "UFNGetIntFromJSONArray": GetIntFromJSONArray,
    "UFNGetStringFromJSONArray": GetStringFromJSONArray,
    "UFNGradualColorMix": GradualColorMix,
    "UFNGrayscaleColorImage": GrayscaleColorImage,
    "UFNLatentImageToVideo": WanLatentImageToVideo,
    "UFNLatentImageToVideoB": WanImageToVideoAlt,
    "UFNLatentPadder": LatentPadder,
    "UFNLatentSelector": LatentSelector,
    "UFNLoadAudioFromAbsolutePath": LoadAudioFromAbs,
    "UFNLoadImagesFromAbsolutePath": LoadImagesFromAbs,
    "UFNLoadLatentFromAbsolutePath": LoadLatentFromAbs,
    "UFNLoadLatentFromOutput": LoadLatentFromOutput,
    "UFNLoadSingleAudioFromAbsolutePath": LoadSingleAudioFromAbs,
    "UFNLoadStringFromAbsolutePath": LoadStringFromAbs,
    "UFNMergeAudioWithTransition": MergeAudioWithTransition,
    "UFNParseJSONArray": ParseJSONArray,
    "UFNSaveAudioToAbsolutePath": SaveAudioToAbs,
    "UFNSaveImagesToAbsolutePath": SaveImagesToAbs,
    "UFNSaveLatentToAbsolutePath": SaveLatentToAbs,
    "UFNSaveStringToAbsolutePath": SaveStringToAbs,
    "UFNSliceJSONArray": SliceJSONArray,
    "UFNSolidColorImage": SolidColorImage,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "UFNAdjustMaskValue": "UFN Adjust Mask Value",
    "UFNArrayToJSONDict": "UFN Array to JSON Dict",
    "UFNConcatJSONArray": "UFN Concatenate JSON Arrays",
    "UFNConcatLatent": "UFN Concatenate Latent",
    "UFNGetFloatFromJSONArray": "UFN Get Float from JSON Array",
    "UFNGetIntFromJSONArray": "UFN Get Int from JSON Array",
    "UFNGetStringFromJSONArray": "UFN Get String from JSON Array",
    "UFNGradualColorMix": "UFN Gradual Color Mix",
    "UFNGrayscaleColorImage": "UFN Grayscale Color Image",
    "UFNLatentImageToVideo": "UFN Latent Image to Video",
    "UFNLatentImageToVideoB": "UFN Latent Image to Video (Alt)",
    "UFNLatentPadder": "UFN Latent Padder",
    "UFNLatentSelector": "UFN Latent Selector",
    "UFNLoadAudioFromAbsolutePath": "UFN Load Audio (Absolute Path)",
    "UFNLoadImagesFromAbsolutePath": "UFN Load Images (Absolute Path)",
    "UFNLoadLatentFromAbsolutePath": "UFN Load Latent (Absolute Path)",
    "UFNLoadLatentFromOutput": "UFN Load Latent (Output)",
    "UFNLoadSingleAudioFromAbsolutePath": "UFN Load Single Audio (Absolute Path)",
    "UFNLoadStringFromAbsolutePath": "UFN Load String (Absolute Path)",
    "UFNMergeAudioWithTransition": "UFN Merge Audio with Transition",
    "UFNParseJSONArray": "UFN Parse JSON Array",
    "UFNSaveAudioToAbsolutePath": "UFN Save Audio (Absolute Path)",
    "UFNSaveImagesToAbsolutePath": "UFN Save Images (Absolute Path)",
    "UFNSaveLatentToAbsolutePath": "UFN Save Latent (Absolute Path)",
    "UFNSaveStringToAbsolutePath": "UFN Save String (Absolute Path)",
    "UFNSliceJSONArray": "UFN Slice JSON Array",
    "UFNSolidColorImage": "UFN Solid Color Image",
}
