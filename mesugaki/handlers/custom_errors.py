import re
from mesugaki.data import register_exception

@register_exception("ConnectionError")
def handle_connection_error(text):
    return "杂鱼~ 连网都连不上！人家才不帮你修呢~"

@register_exception("TimeoutError")
def handle_timeout_error(text):
    return "笨蛋！等这么久，蜗牛都比你快！"