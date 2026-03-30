import json


class GetIntFromJSONArray:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "array_json": ("STRING",),
                "index": ("INT", {"default": 0, "min": -99999, "max": 99999, "step": 1}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("INT",)
    FUNCTION = "get_item"
    TITLE = "Get Int from JSON Array"

    def get_item(self, array_json, index):
        array = json.loads(array_json)

        if not isinstance(array, list):
            raise ValueError(f"Input must be a JSON array, got {type(array).__name__}")

        return (int(array[index]),)
