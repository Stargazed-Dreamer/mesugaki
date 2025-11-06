class _GlobalRegistry:
    """全局注册表，管理所有异常处理器"""

    def __init__(self):
        self._handlers = {}
        self._default_handler = Mesugaki

    def register(self, exc_type, handler_func):
        """注册异常处理器"""
        self._handlers[exc_type] = handler_func

    def unregister(self, exc_type):
        """注销异常处理器"""
        return self._handlers.pop(exc_type, None)

    def get_handler(self, exc_type):
        """获取异常处理器"""
        return self._handlers.get(exc_type, self._default_handler)

    def set_default(self, handler_class):
        """设置默认处理器"""
        self._default_handler = handler_class


# 全局注册表实例
_registry = _GlobalRegistry()


# ==================== 公共扩展接口 ====================
def register_handler(exc_type, handler_func=None):
    """装饰器：注册异常处理器

    用法1：作为装饰器
    @register_handler(ValueError)
    def handle_value_error(error_text):
        return "你的值有问题啦~"

    用法2：直接注册
    register_handler(ValueError, handle_value_error)
    """

    def decorator(func):
        _registry.register(exc_type.__name__, func)
        return func

    if handler_func is None:
        return decorator
    else:
        _registry.register(exc_type.__name__, handler_func)
        return handler_func


def unregister_handler(exc_type):
    """注销异常处理器"""
    return _registry.unregister(exc_type.__name__)