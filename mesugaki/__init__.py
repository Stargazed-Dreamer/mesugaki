import sys
from traceback import format_exception
from .main import Mesugaki

__all__ = ["Mesugaki", "alwaysMesugaki", "stopMesugaki"]

# ========================================
# 自动载入覆盖的错误提示
import importlib
from pathlib import Path

def _load_handlers():
    """自动加载handlers目录下的所有模块"""
    handlers_dir = Path(__file__).parent / "handlers"
    if not handlers_dir.exists():
        return
    
    for module_file in handlers_dir.glob("*.py"):
        if module_file.name.startswith("_"):
            continue
        module_name = f"mesugaki.handlers.{module_file.stem}"
        importlib.import_module(module_name)
# 在包初始化时加载
_load_handlers()

# ========================================
# 延迟初始化控制 - 用于实现import alwaysMesugaki即启动
_installed = False
_original_excepthook = None

def _install_global_hook():
    global _installed, _original_excepthook
    if not _installed:
        _original_excepthook = sys.excepthook

        def _global_hook(exc_type, exc_value, exc_tb):
            l_traceback = format_exception(exc_type, exc_value, exc_tb)
            m = Mesugaki()
            m.handle_output(exc_type, exc_value, l_traceback)

        sys.excepthook = _global_hook
        _installed = True

def _uninstall_global_hook():
    global _installed, _original_excepthook
    if _installed and _original_excepthook is not None:
        sys.excepthook = _original_excepthook
        _installed = False

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
