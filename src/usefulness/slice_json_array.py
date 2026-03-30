import json


class SliceJSONArray:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "array_json": ("STRING",),
                "start_index": ("INT", {"default": 0, "min": -99999, "max": 99999, "step": 1}),
                "end_index": ("INT", {"default": -1, "min": -99999, "max": 99999, "step": 1}),
                "use_end_index": ("BOOLEAN", {"default": True}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("array_json",)
    FUNCTION = "slice_array"
    TITLE = "Slice JSON Array"

    def slice_array(self, array_json, start_index, end_index, use_end_index):
        array = json.loads(array_json)

        if not isinstance(array, list):
            raise ValueError(f"Input must be a JSON array, got {type(array).__name__}")

        if not use_end_index:
            result = array[start_index:]
        else:
            result = array[start_index:end_index]

        return (json.dumps(result),)
