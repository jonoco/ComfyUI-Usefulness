import json


class GetStringFromJSONDict:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dict_json": ("STRING",),
                "key": ("STRING", {"default": ""}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("value",)
    FUNCTION = "get_string"
    TITLE = "Get String from JSON Dict"

    def get_string(self, dict_json, key):
        data = json.loads(dict_json)

        if not isinstance(data, dict):
            raise ValueError(f"Input must be a JSON dictionary, got {type(data).__name__}")

        if key not in data:
            raise KeyError(f"Key '{key}' not found in dictionary")

        return (str(data[key]),)
