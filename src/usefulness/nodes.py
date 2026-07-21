from .add_string_to_json_dict import AddStringToJSONDict
from .adjust_mask_value import AdjustMaskValue
from .array_to_json_dict import ArrayToJSONDict
from .color_mix import GradualColorMix
from .concat_json_array import ConcatJSONArray
from .concat_latent import ContatenatedLatent
from .get_float_from_array import GetFloatFromJSONArray
from .get_int_from_array import GetIntFromJSONArray
from .get_string_from_array import GetStringFromJSONArray
from .get_string_from_json_dict import GetStringFromJSONDict
from .grayscale_color import GrayscaleColorImage
from .load_audio_abs import LoadAudioFromAbs
from .load_audio_single import LoadSingleAudioFromAbs
from .load_images_abs import LoadImagesFromAbs
from .load_latent_abs import LoadLatentFromAbs
from .load_string_abs import LoadStringFromAbs
from .merge_audio_with_transition import MergeAudioWithTransition
from .parse_json_array import ParseJSONArray
from .resample_audio import ResampleAudio
from .save_audio_abs import SaveAudioToAbs
from .save_images_abs import SaveImagesToAbs
from .save_latent_abs import SaveLatentToAbs
from .save_string_abs import SaveStringToAbs
from .select_latent import LatentSelector
from .slice_json_array import SliceJSONArray
from .solid_color import SolidColorImage

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "UFNAddStringToJSONDict": AddStringToJSONDict,
    "UFNAdjustMaskValue": AdjustMaskValue,
    "UFNArrayToJSONDict": ArrayToJSONDict,
    "UFNConcatJSONArray": ConcatJSONArray,
    "UFNConcatLatent": ContatenatedLatent,
    "UFNGetFloatFromJSONArray": GetFloatFromJSONArray,
    "UFNGetIntFromJSONArray": GetIntFromJSONArray,
    "UFNGetStringFromJSONArray": GetStringFromJSONArray,
    "UFNGetStringFromJSONDict": GetStringFromJSONDict,
    "UFNGradualColorMix": GradualColorMix,
    "UFNGrayscaleColorImage": GrayscaleColorImage,
    "UFNLatentSelector": LatentSelector,
    "UFNLoadAudioFromAbsolutePath": LoadAudioFromAbs,
    "UFNLoadImagesFromAbsolutePath": LoadImagesFromAbs,
    "UFNLoadLatentFromAbsolutePath": LoadLatentFromAbs,
    "UFNLoadSingleAudioFromAbsolutePath": LoadSingleAudioFromAbs,
    "UFNLoadStringFromAbsolutePath": LoadStringFromAbs,
    "UFNMergeAudioWithTransition": MergeAudioWithTransition,
    "UFNParseJSONArray": ParseJSONArray,
    "UFNResampleAudio": ResampleAudio,
    "UFNSaveAudioToAbsolutePath": SaveAudioToAbs,
    "UFNSaveImagesToAbsolutePath": SaveImagesToAbs,
    "UFNSaveLatentToAbsolutePath": SaveLatentToAbs,
    "UFNSaveStringToAbsolutePath": SaveStringToAbs,
    "UFNSliceJSONArray": SliceJSONArray,
    "UFNSolidColorImage": SolidColorImage,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "UFNAddStringToJSONDict": "UFN Add String to JSON Dict",
    "UFNAdjustMaskValue": "UFN Adjust Mask Value",
    "UFNArrayToJSONDict": "UFN Array to JSON Dict",
    "UFNConcatJSONArray": "UFN Concatenate JSON Arrays",
    "UFNConcatLatent": "UFN Concatenate Latent",
    "UFNGetFloatFromJSONArray": "UFN Get Float from JSON Array",
    "UFNGetIntFromJSONArray": "UFN Get Int from JSON Array",
    "UFNGetStringFromJSONArray": "UFN Get String from JSON Array",
    "UFNGetStringFromJSONDict": "UFN Get String from JSON Dict",
    "UFNGradualColorMix": "UFN Gradual Color Mix",
    "UFNGrayscaleColorImage": "UFN Grayscale Color Image",
    "UFNLatentSelector": "UFN Latent Selector",
    "UFNLoadAudioFromAbsolutePath": "UFN Load Audio (Absolute Path)",
    "UFNLoadImagesFromAbsolutePath": "UFN Load Images (Absolute Path)",
    "UFNLoadLatentFromAbsolutePath": "UFN Load Latent (Absolute Path)",
    "UFNLoadSingleAudioFromAbsolutePath": "UFN Load Single Audio (Absolute Path)",
    "UFNLoadStringFromAbsolutePath": "UFN Load String (Absolute Path)",
    "UFNMergeAudioWithTransition": "UFN Merge Audio with Transition",
    "UFNParseJSONArray": "UFN Parse JSON Array",
    "UFNResampleAudio": "UFN Resample Audio",
    "UFNSaveAudioToAbsolutePath": "UFN Save Audio (Absolute Path)",
    "UFNSaveImagesToAbsolutePath": "UFN Save Images (Absolute Path)",
    "UFNSaveLatentToAbsolutePath": "UFN Save Latent (Absolute Path)",
    "UFNSaveStringToAbsolutePath": "UFN Save String (Absolute Path)",
    "UFNSliceJSONArray": "UFN Slice JSON Array",
    "UFNSolidColorImage": "UFN Solid Color Image",
}
