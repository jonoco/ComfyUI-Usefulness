import json


class ParseJSONArray:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_string": ("STRING",),
                "key": ("STRING", {"default": ""}),
                "start_index": ("INT", {"default": 0}),
                "end_index": ("INT", {"default": -1}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("array_json",)
    FUNCTION = "parse_array"
    TITLE = "Parse JSON Array"

    def parse_array(self, json_string, key, start_index, end_index):
        data = json.loads(json_string)

        if key:
            array = data[key]
        else:
            array = data

        if end_index == -1:
            result = array[start_index:]
        else:
            result = array[start_index:end_index + 1]

        return (json.dumps(result),)
