import json


class ConcatJSONArray:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "array_json_1": ("STRING",),
                "array_json_2": ("STRING",),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("array_json",)
    FUNCTION = "concat_arrays"
    TITLE = "Concatenate JSON Arrays"

    def concat_arrays(self, array_json_1, array_json_2):
        array_1 = json.loads(array_json_1)
        array_2 = json.loads(array_json_2)

        if not isinstance(array_1, list):
            raise ValueError(f"First input must be a JSON array, got {type(array_1).__name__}")
        if not isinstance(array_2, list):
            raise ValueError(f"Second input must be a JSON array, got {type(array_2).__name__}")

        result = array_1 + array_2
        return (json.dumps(result),)
