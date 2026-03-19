import os


class SaveStringToAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "file_path": ("STRING", {"default": ""}),
                "append": ("BOOLEAN", {"default": False}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ()
    FUNCTION = "save_string"
    TITLE = "Save String (Absolute Path)"
    OUTPUT_NODE = True

    def save_string(self, text, file_path, append):
        # Ensure directory exists
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        mode = "a" if append else "w"
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(text)

        return {}
