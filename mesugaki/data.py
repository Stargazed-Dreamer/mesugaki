import re
from hashlib import sha512
from time import time
from typing import Dict, Callable, Optional

s_hearts = "❤🧡💛💚💙💜"

def heart(index=None):
    '''在爱心表里随机或者指定一个爱心返回'''
    if index is None:
        seed = time()
        index = int(sha512(str(seed).encode('utf-8')).hexdigest(), base=16) % len(s_hearts)
    return s_hearts[index]

#================================================

class _ExceptionHandler:
    def __init__(self):
        self.d_table: Dict[str, Callable] = {}
        self._load_builtin_handlers()
    
    def register(self, exception_name: str, handler: Callable):
        """注册异常处理函数"""
        self.d_table[exception_name] = handler
    
    def _load_builtin_handlers(self):
        """加载内置异常处理"""
        # 自动扫描所有以 _handle_ 开头的方法
        for method_name in dir(self):
            if method_name.startswith("_handle_"):
                exception_name = method_name[8:]  # 去掉 "_handle_" 前缀
                if exception_name not in self.d_table:
                    self.register(exception_name, getattr(self, method_name))

class ExceptionHandler(_ExceptionHandler):
    """异常处理器，提供正常的异常处理模式"""
    
    # 基础异常类
    def _handle_BaseException(self, text: str) -> Optional[str]:
        return f"基础异常: {text}"
    
    def _handle_SystemExit(self, text: str) -> Optional[str]:
        return f"系统退出: {text}"
    
    def _handle_KeyboardInterrupt(self, text: str) -> Optional[str]:
        return "用户中断执行 (Ctrl+C)"
    
    def _handle_GeneratorExit(self, text: str) -> Optional[str]:
        return "生成器关闭异常"
    
    # 常规异常基类
    def _handle_Exception(self, text: str) -> Optional[str]:
        return f"常规异常: {text}"
    
    # 迭代相关异常
    def _handle_StopIteration(self, text: str) -> Optional[str]:
        return "迭代器已耗尽，没有更多值"
    
    def _handle_StopAsyncIteration(self, text: str) -> Optional[str]:
        return "异步迭代器已耗尽，没有更多值"
    
    # 算术错误
    def _handle_ArithmeticError(self, text: str) -> Optional[str]:
        return f"算术错误: {text}"
    
    def _handle_FloatingPointError(self, text: str) -> Optional[str]:
        return "浮点数计算错误"
    
    def _handle_OverflowError(self, text: str) -> Optional[str]:
        return "数值运算结果太大，无法表示"
    
    def _handle_ZeroDivisionError(self, text: str) -> Optional[str]:
        return "除零错误：除数不能为零"
    
    # 断言和属性错误
    def _handle_AssertionError(self, text: str) -> Optional[str]:
        return f"断言失败: {text}"
    
    def _handle_AttributeError(self, text: str) -> Optional[str]:
        compile_AttributeError = re.compile(r".*'(.*)' object has no attribute '(.*)'")
        if result := compile_AttributeError.match(text):
            obj_type, attr = result.groups()
            return f"属性错误: '{obj_type}' 对象没有属性 '{attr}'"
        return f"属性错误: {text}"
    
    # 缓冲区和IO错误
    def _handle_BufferError(self, text: str) -> Optional[str]:
        return f"缓冲区操作错误: {text}"
    
    def _handle_EOFError(self, text: str) -> Optional[str]:
        return "文件结束错误：输入函数在没有读取任何数据时遇到EOF"
    
    # 导入错误
    def _handle_ImportError(self, text: str) -> Optional[str]:
        return f"导入错误: {text}"
    
    def _handle_ModuleNotFoundError(self, text: str) -> Optional[str]:
        compile_ModuleNotFound = re.compile(r"No module named '(.*)'")
        if result := compile_ModuleNotFound.match(text):
            module = result.groups()[0]
            return f"模块未找到: 无法导入模块 '{module}'"
        return f"模块未找到: {text}"
    
    # 查找错误
    def _handle_LookupError(self, text: str) -> Optional[str]:
        return f"查找错误: {text}"
    
    def _handle_IndexError(self, text: str) -> Optional[str]:
        return "索引错误：序列索引超出范围"
    
    def _handle_KeyError(self, text: str) -> Optional[str]:
        compile_KeyError = re.compile(r"'(.*)'")
        if result := compile_KeyError.search(text):
            key = result.groups()[0]
            return f"键错误: 映射中不存在键 '{key}'"
        return f"键错误: {text}"
    
    # 内存错误
    def _handle_MemoryError(self, text: str) -> Optional[str]:
        return "内存错误：内存不足"
    
    # 名称错误
    def _handle_NameError(self, text: str) -> Optional[str]:
        compile_NameError = re.compile(r"name '(.*)' is not defined")
        if result := compile_NameError.match(text):
            name = result.groups()[0]
            return f"名称错误: 名称 '{name}' 未定义"
        return f"名称错误: {text}"
    
    def _handle_UnboundLocalError(self, text: str) -> Optional[str]:
        compile_UnboundLocal = re.compile(r"local variable '(.*)' referenced before assignment")
        if result := compile_UnboundLocal.match(text):
            var = result.groups()[0]
            return f"未绑定局部变量: 局部变量 '{var}' 在赋值前被引用"
        return f"未绑定局部变量: {text}"
    
    # 操作系统错误
    def _handle_OSError(self, text: str) -> Optional[str]:
        return f"操作系统错误: {text}"
    
    def _handle_BlockingIOError(self, text: str) -> Optional[str]:
        return "阻塞IO错误：操作将阻塞对象设置为非阻塞操作"
    
    def _handle_ChildProcessError(self, text: str) -> Optional[str]:
        return "子进程错误：子进程上的操作失败"
    
    # 连接错误
    def _handle_ConnectionError(self, text: str) -> Optional[str]:
        return f"连接错误: {text}"
    
    def _handle_BrokenPipeError(self, text: str) -> Optional[str]:
        return "管道破裂错误：另一端已关闭"
    
    def _handle_ConnectionAbortedError(self, text: str) -> Optional[str]:
        return "连接中止错误：连接尝试被对等方中止"
    
    def _handle_ConnectionRefusedError(self, text: str) -> Optional[str]:
        return "连接拒绝错误：连接尝试被对等方拒绝"
    
    def _handle_ConnectionResetError(self, text: str) -> Optional[str]:
        return "连接重置错误：连接由对等方重置"
    
    # 文件系统错误
    def _handle_FileExistsError(self, text: str) -> Optional[str]:
        compile_FileExists = re.compile(r".*'(.*)'")
        if result := compile_FileExists.search(text):
            path = result.groups()[0]
            return f"文件存在错误: 文件或目录 '{path}' 已存在"
        return f"文件存在错误: {text}"
    
    def _handle_FileNotFoundError(self, text: str) -> Optional[str]:
        compile_FileNotFound = re.compile(r".*'(.*)'")
        if result := compile_FileNotFound.search(text):
            path = result.groups()[0]
            return f"文件未找到错误: 文件或目录 '{path}' 不存在"
        return f"文件未找到错误: {text}"
    
    def _handle_InterruptedError(self, text: str) -> Optional[str]:
        return "中断错误：系统调用被输入信号中断"
    
    def _handle_IsADirectoryError(self, text: str) -> Optional[str]:
        return "目录错误：在目录上请求了文件操作"
    
    def _handle_NotADirectoryError(self, text: str) -> Optional[str]:
        return "非目录错误：在非目录对象上请求了目录操作"
    
    def _handle_PermissionError(self, text: str) -> Optional[str]:
        return "权限错误：没有足够的访问权限执行操作"
    
    def _handle_ProcessLookupError(self, text: str) -> Optional[str]:
        return "进程查找错误：给定的进程不存在"
    
    def _handle_TimeoutError(self, text: str) -> Optional[str]:
        return "超时错误：系统函数在系统级别超时"
    
    # 引用错误
    def _handle_ReferenceError(self, text: str) -> Optional[str]:
        return "引用错误：弱引用试图访问已垃圾回收的对象"
    
    # 运行时错误
    def _handle_RuntimeError(self, text: str) -> Optional[str]:
        return f"运行时错误: {text}"
    
    def _handle_NotImplementedError(self, text: str) -> Optional[str]:
        return "未实现错误：方法或功能尚未实现"
    
    def _handle_RecursionError(self, text: str) -> Optional[str]:
        return "递归错误：超出最大递归深度"
    
    # 语法错误
    def _handle_SyntaxError(self, text: str) -> Optional[str]:
        return f"语法错误: {text}"
    
    def _handle_IndentationError(self, text: str) -> Optional[str]:
        return "缩进错误：代码缩进不正确"
    
    def _handle_TabError(self, text: str) -> Optional[str]:
        return "制表符错误：Tab和空格混用"
    
    # 系统错误
    def _handle_SystemError(self, text: str) -> Optional[str]:
        return f"系统错误: {text}"
    
    # 类型错误
    def _handle_TypeError(self, text: str) -> Optional[str]:
        compile_TypeError_1 = re.compile(r"(.*) takes ([0-9]+) positional argument but ([0-9]+) (?:were|was) given")
        compile_TypeError_2 = re.compile(r"(.*) missing ([0-9]+) required positional (?:arguments|argument): (?:'(.*)')+ (?:and '(.*)')?")
        compile_TypeError_3 = re.compile(r"(.*)() argument must be (.+), not (.+)")
        
        if result := compile_TypeError_1.match(text):
            func_name, expected, given = result.groups()
            return f"类型错误: 函数 '{func_name}' 接受 {expected} 个位置参数，但给出了 {given} 个"
        elif result := compile_TypeError_2.match(text):
            func_name, count, *args = result.groups()
            args = [arg for arg in args if arg is not None]
            args_str = ", ".join(f"'{arg}'" for arg in args)
            return f"类型错误: 函数 '{func_name}' 缺少 {count} 个必需的位置参数: {args_str}"
        elif result := compile_TypeError_3.match(text):
            func_name, arg_name, expected_type, actual_type = result.groups()
            return f"类型错误: 参数 '{arg_name}' 必须是 {expected_type} 类型，不是 {actual_type}"
        return f"类型错误: {text}"
    
    # 值错误
    def _handle_ValueError(self, text: str) -> Optional[str]:
        return f"值错误: {text}"
    
    # Unicode错误
    def _handle_UnicodeError(self, text: str) -> Optional[str]:
        return f"Unicode错误: {text}"
    
    def _handle_UnicodeDecodeError(self, text: str) -> Optional[str]:
        compile_UnicodeDecode = re.compile(r"'(.*)' codec can't decode byte (0x[0-9a-f]+) in position ([0-9]+): (.*)")
        if result := compile_UnicodeDecode.match(text):
            codec, byte, pos, reason = result.groups()
            return f"Unicode解码错误: '{codec}' 编解码器无法解码位置 {pos} 的字节 {byte}: {reason}"
        return f"Unicode解码错误: {text}"
    
    def _handle_UnicodeEncodeError(self, text: str) -> Optional[str]:
        compile_UnicodeEncode = re.compile(r"'(.*)' codec can't encode character '(.*)' in position ([0-9]+): (.*)")
        if result := compile_UnicodeEncode.match(text):
            codec, char, pos, reason = result.groups()
            return f"Unicode编码错误: '{codec}' 编解码器无法编码位置 {pos} 的字符 '{char}': {reason}"
        return f"Unicode编码错误: {text}"
    
    def _handle_UnicodeTranslateError(self, text: str) -> Optional[str]:
        return f"Unicode转码错误: {text}"
    
    # 警告类
    def _handle_Warning(self, text: str) -> Optional[str]:
        return f"警告: {text}"
    
    def _handle_DeprecationWarning(self, text: str) -> Optional[str]:
        return "弃用警告：使用了已弃用的功能"
    
    def _handle_PendingDeprecationWarning(self, text: str) -> Optional[str]:
        return "即将弃用警告：使用了计划弃用的功能"
    
    def _handle_RuntimeWarning(self, text: str) -> Optional[str]:
        return f"运行时警告: {text}"
    
    def _handle_SyntaxWarning(self, text: str) -> Optional[str]:
        return f"语法警告: {text}"
    
    def _handle_UserWarning(self, text: str) -> Optional[str]:
        return f"用户警告: {text}"
    
    def _handle_FutureWarning(self, text: str) -> Optional[str]:
        return "未来警告：使用了将在未来版本中改变的行为"
    
    def _handle_ImportWarning(self, text: str) -> Optional[str]:
        return f"导入警告: {text}"
    
    def _handle_UnicodeWarning(self, text: str) -> Optional[str]:
        return f"Unicode警告: {text}"
    
    def _handle_BytesWarning(self, text: str) -> Optional[str]:
        return f"字节警告: {text}"
    
    def _handle_ResourceWarning(self, text: str) -> Optional[str]:
        return f"资源警告: {text}"

# 全局异常处理器实例
exception_handler = ExceptionHandler()

# 装饰器函数
def register_exception(exception_name: str):
    """异常处理注册装饰器"""
    def decorator(func: Callable):
        exception_handler.register(exception_name, func)
        return func
    return decorator