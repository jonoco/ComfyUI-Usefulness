import os
import hashlib


class LoadStringFromAbs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "file_path": ("STRING", {"default": ""}),
            }
        }

    CATEGORY = "utils"
    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_string"
    TITLE = "Load String (Absolute Path)"

    def load_string(self, file_path):
        if not os.path.exists(file_path):
            raise ValueError(f"File not found at path: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        return (text,)

    @classmethod
    def IS_CHANGED(s, file_path):
        if not os.path.exists(file_path):
            return ""
        m = hashlib.sha256()
        with open(file_path, "rb") as f:
            m.update(f.read())
        return m.digest().hex()
