import sys
import re
from traceback import format_exception
from .main import Mesugaki

__all__ = ["Mesugaki", "alwaysMesugaki", "stopMesugaki"]

_installed = False
_original_excepthook = None


def _install_global_hook():
    global _installed, _original_excepthook
    if not _installed:
        _original_excepthook = sys.excepthook

        def _global_hook(exc_type, exc_value, exc_tb):
            l_traceback = format_exception(exc_type, exc_value, exc_tb)
            m = Mesugaki()
            m.output = ""
            m.compile_fileLine = re.compile(' *File "(.+)", line ([0-9]+), in (.+)')

            # 复制 main.py 中的处理逻辑
            m.add(f"笨 蛋 ！ 蟒蛇都能写错~")

            # 堆栈字符串列表预处理
            l_error = []
            for string in l_traceback:
                l_lines = string.split("\n")
                if "" in l_lines:
                    l_lines.remove("")
                l_error += l_lines

            assert l_error.pop(0) == "Traceback (most recent call last):"
            originalExceptionText = l_error.pop(-1)

            m.loop_main(l_error)
            exceptionText = m.error(exc_type.__name__, str(exc_value))
            m.add(exceptionText)

            print(m.output)

        sys.excepthook = _global_hook
        _installed = True


def _uninstall_global_hook():
    global _installed, _original_excepthook
    if _installed and _original_excepthook is not None:
        sys.excepthook = _original_excepthook
        _installed = False


# ==================== 延迟初始化控制 ====================
class _AlwaysMesugaki:
    def __init__(self):
        _install_global_hook()

    def __del__(self):
        _uninstall_global_hook()

    def stop(self):
        self.__del__()

def _get_always_mesugaki():
    if not hasattr(__name__, "alwaysMesugaki"):
        global alwaysMesugaki
        alwaysMesugaki = _AlwaysMesugaki()
    return alwaysMesugaki

def __getattr__(name):
    if name == "alwaysMesugaki":
        return _get_always_mesugaki()
    elif name == "stopMesugaki":
        _uninstall_global_hook()
        return None
    raise AttributeError(f"module {__name__} has no attribute {name}")
