from .main import Mesugaki

class _AlwaysMesugaki:
    """只要被 import 一次，就自动把 Mesugaki 钩到 sys.excepthook 上，等同于『with Mesugaki():』永不过期。"""
    _installed = False

    def __init__(self):
        # 防止重复安装
        if _AlwaysMesugaki._installed:
            return
        _AlwaysMesugaki._installed = True

        # 把 Mesugaki 上下文管理器永久激活
        self._mgr = Mesugaki()
        self._mgr.__enter__()

        # 进程正常退出时再清理，防止上下文管理器报警告
        import atexit
        atexit.register(self._cleanup)

    def _cleanup(self):
        self._mgr.__exit__(None, None, None)

alwaysMesugaki = _AlwaysMesugaki()