import json


class ArrayToJSONDict:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "array_json": ("STRING",),
                "key": ("STRING", {"default": ""}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dict_json",)
    FUNCTION = "array_to_dict"
    TITLE = "Array to JSON Dict"

    def array_to_dict(self, array_json, key):
        array = json.loads(array_json)

        if not isinstance(array, list):
            raise ValueError(f"Input must be a JSON array, got {type(array).__name__}")

        result = {key: array}
        return (json.dumps(result),)
