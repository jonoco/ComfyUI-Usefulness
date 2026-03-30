import json


class ParseJSONArray:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "json_string": ("STRING",),
                "key": ("STRING", {"default": ""}),
                "start_index": ("INT", {"default": 0, "min": -99999, "max": 99999, "step": 1}),
                "end_index": ("INT", {"default": -1, "min": -99999, "max": 99999, "step": 1}),
                "use_end_index": ("BOOLEAN", {"default": True}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("array_json",)
    FUNCTION = "parse_array"
    TITLE = "Parse JSON Array"

    def parse_array(self, json_string, key, start_index, end_index, use_end_index):
        data = json.loads(json_string)

        if key:
            array = data[key]
        else:
            array = data

        if not use_end_index:
            result = array[start_index:]
        else:
            result = array[start_index:end_index]

        return (json.dumps(result),)
