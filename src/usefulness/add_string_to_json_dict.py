import json


class AddStringToJSONDict:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dict_json": ("STRING",),
                "key": ("STRING", {"default": ""}),
                "value": ("STRING", {"default": ""}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dict_json",)
    FUNCTION = "add_string"
    TITLE = "Add String to JSON Dict"

    def add_string(self, dict_json, key, value):
        data = json.loads(dict_json)

        if not isinstance(data, dict):
            raise ValueError(f"Input must be a JSON dictionary, got {type(data).__name__}")

        data[key] = value
        return (json.dumps(data),)
