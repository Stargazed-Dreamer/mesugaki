from mesugaki.data import register_exception
import re

@register_exception("KeyError")
def handle_key_error(text: str):
    match = re.search(r"'(.+)'", text)
    key = match.group(1) if match else "某个东西"
    return f"哼！{key}？人家才没有这种东西呢~"