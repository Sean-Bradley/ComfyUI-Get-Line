class GetLine:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "index": ("INT", {
                    "default": 0,
                    "min": 0,
                    "step": 1,
                    "display": "number",
                    "control_after_generate": "increment"
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("line",)
    FUNCTION = "get_line"
    CATEGORY = "SBCODE"

    def get_line(self, text, index):
        lines = text.splitlines()

        if not lines:
            return ("",)

        safe_index = max(0, min(index, len(lines) - 1))
        return (lines[safe_index],)


NODE_CLASS_MAPPINGS = {
    "Get Line": GetLine
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Get Line": "Get Line"
}
