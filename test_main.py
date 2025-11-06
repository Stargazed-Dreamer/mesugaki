import unittest
#============================
from mesugaki import Mesugaki

class Mesugaki(Mesugaki):
    def __init__(self, exception=None):
        super().__init__()
        if exception is not None:
            self.s_onlyException = exception.__name__
        else:
            self.s_onlyException = "undefined"

    def error(self, errorType, errorText):
        '''将错误信息重写'''
        if errorType != self.s_onlyException:
            raise KeyError(f"没有犯 {self.s_onlyException} 错误？只是不小心犯下 {errorType} ？聪…聪明？才怪，还是笨蛋啦~")
        elif errorType not in self.d_table:
            raise KeyError(f"犯 {self.s_onlyException} 错误却不告诉我怎么处理？聪…聪明？才怪，还是笨蛋啦~")
        else:
            string = self.d_table[errorType](errorText)
        return string

#Mesugaki.use_original_location_hint = True

class Test(unittest.TestCase):
    #example
    def test_Exception(self):
        with Mesugaki(Exception):
            raise Exception("example")
    
    def test_MemoryError(self):
        with Mesugaki(MemoryError):
            try:
                "a" * 10**9  # 尝试分配大量内存
            except MemoryError:
                raise MemoryError("内存溢出测试")
    
    def test_AttributeError(self):
        with Mesugaki(AttributeError):
            "a".test

    def test_TypeError(self):
        #1
        with Mesugaki(TypeError):
            def a(aa):
                pass
            a(1,1)
        #2
        with Mesugaki(TypeError):
            def a(aa, bb):
                pass
            a()
    
    def test_ZeroDivisionError(self):
        with Mesugaki(ZeroDivisionError):
            1/0
    
    def test_BaseException(self):
        with Mesugaki(BaseException):
            raise BaseException("基础异常测试")
    
    def test_SystemExit(self):
        with Mesugaki(SystemExit):
            raise SystemExit("系统退出测试")
    
    def test_KeyboardInterrupt(self):
        with Mesugaki(KeyboardInterrupt):
            raise KeyboardInterrupt("键盘中断测试")
    
    def test_GeneratorExit(self):
        with Mesugaki(GeneratorExit):
            raise GeneratorExit("生成器退出测试")
    
    def test_StopIteration(self):
        with Mesugaki(StopIteration):
            def gen():
                yield 1
                raise StopIteration("迭代器耗尽测试")
            g = gen()
            next(g)
            next(g)
    
    def test_StopAsyncIteration(self):
        with Mesugaki(StopAsyncIteration):
            raise StopAsyncIteration("异步迭代器耗尽测试")
    
    def test_ArithmeticError(self):
        with Mesugaki(ArithmeticError):
            raise ArithmeticError("算术错误测试")
    
    def test_FloatingPointError(self):
        with Mesugaki(FloatingPointError):
            import math
            try:
                math.exp(1000)  # 可能导致浮点溢出
            except OverflowError:
                raise FloatingPointError("浮点错误测试")
    
    def test_OverflowError(self):
        with Mesugaki(OverflowError):
            10 ** 1000  # 大数溢出
    
    def test_AssertionError(self):
        with Mesugaki(AssertionError):
            assert False, "断言失败测试"
    
    def test_BufferError(self):
        with Mesugaki(BufferError):
            raise BufferError("缓冲区错误测试")
    
    def test_EOFError(self):
        with Mesugaki(EOFError):
            raise EOFError("文件结束错误测试")
    
    def test_ImportError(self):
        with Mesugaki(ImportError):
            raise ImportError("导入错误测试")
    
    def test_ModuleNotFoundError(self):
        with Mesugaki(ModuleNotFoundError):
            raise ModuleNotFoundError("模块未找到测试")
    
    def test_LookupError(self):
        with Mesugaki(LookupError):
            raise LookupError("查找错误测试")
    
    def test_IndexError(self):
        with Mesugaki(IndexError):
            lst = [1, 2, 3]
            lst[10]
    
    def test_KeyError(self):
        with Mesugaki(KeyError):
            d = {"a": 1}
            d["b"]
    
    def test_NameError(self):
        with Mesugaki(NameError):
            undefined_variable
    
    def test_UnboundLocalError(self):
        with Mesugaki(UnboundLocalError):
            def test():
                x = x + 1
            test()
    
    def test_OSError(self):
        with Mesugaki(OSError):
            raise OSError("操作系统错误测试")
    
    def test_BlockingIOError(self):
        with Mesugaki(BlockingIOError):
            raise BlockingIOError("阻塞IO错误测试")
    
    def test_ChildProcessError(self):
        with Mesugaki(ChildProcessError):
            raise ChildProcessError("子进程错误测试")
    
    def test_ConnectionError(self):
        with Mesugaki(ConnectionError):
            raise ConnectionError("连接错误测试")
    
    def test_BrokenPipeError(self):
        with Mesugaki(BrokenPipeError):
            raise BrokenPipeError("管道破裂错误测试")
    
    def test_ConnectionAbortedError(self):
        with Mesugaki(ConnectionAbortedError):
            raise ConnectionAbortedError("连接中止错误测试")
    
    def test_ConnectionRefusedError(self):
        with Mesugaki(ConnectionRefusedError):
            raise ConnectionRefusedError("连接拒绝错误测试")
    
    def test_ConnectionResetError(self):
        with Mesugaki(ConnectionResetError):
            raise ConnectionResetError("连接重置错误测试")
    
    def test_FileExistsError(self):
        with Mesugaki(FileExistsError):
            raise FileExistsError("文件存在错误测试")
    
    def test_FileNotFoundError(self):
        with Mesugaki(FileNotFoundError):
            raise FileNotFoundError("文件未找到错误测试")
    
    def test_InterruptedError(self):
        with Mesugaki(InterruptedError):
            raise InterruptedError("中断错误测试")
    
    def test_IsADirectoryError(self):
        with Mesugaki(IsADirectoryError):
            raise IsADirectoryError("目录错误测试")
    
    def test_NotADirectoryError(self):
        with Mesugaki(NotADirectoryError):
            raise NotADirectoryError("非目录错误测试")
    
    def test_PermissionError(self):
        with Mesugaki(PermissionError):
            raise PermissionError("权限错误测试")
    
    def test_ProcessLookupError(self):
        with Mesugaki(ProcessLookupError):
            raise ProcessLookupError("进程查找错误测试")
    
    def test_TimeoutError(self):
        with Mesugaki(TimeoutError):
            raise TimeoutError("超时错误测试")
    
    def test_ReferenceError(self):
        with Mesugaki(ReferenceError):
            import weakref
            class Test:
                pass
            obj = Test()
            weak_ref = weakref.ref(obj)
            del obj
            try:
                weak_ref()  # 尝试访问已垃圾回收的对象
            except ReferenceError:
                raise ReferenceError("引用错误测试")
    
    def test_RuntimeError(self):
        with Mesugaki(RuntimeError):
            raise RuntimeError("运行时错误测试")
    
    def test_NotImplementedError(self):
        with Mesugaki(NotImplementedError):
            raise NotImplementedError("未实现错误测试")
    
    def test_RecursionError(self):
        with Mesugaki(RecursionError):
            def recursive():
                recursive()
            recursive()
    
    def test_SyntaxError(self):
        with Mesugaki(SyntaxError):
            exec("def test(\n    pass")  # 故意的语法错误
    
    def test_IndentationError(self):
        with Mesugaki(IndentationError):
            exec("def test():\npass")  # 缩进错误
    
    def test_TabError(self):
        with Mesugaki(TabError):
            exec("def test():\n\tpass\n    pass")  # Tab和空格混用
    
    def test_SystemError(self):
        with Mesugaki(SystemError):
            raise SystemError("系统错误测试")
    
    def test_ValueError(self):
        with Mesugaki(ValueError):
            int("abc")
    
    def test_UnicodeError(self):
        with Mesugaki(UnicodeError):
            raise UnicodeError("Unicode错误测试")
    
    def test_UnicodeDecodeError(self):
        with Mesugaki(UnicodeDecodeError):
            b'\xff\xfe'.decode('utf-8')
    
    def test_UnicodeEncodeError(self):
        with Mesugaki(UnicodeEncodeError):
            '\ud800'.encode('utf-8')
    
    def test_UnicodeTranslateError(self):
        with Mesugaki(UnicodeTranslateError):
            raise UnicodeTranslateError("Unicode转码错误测试")
    
    def test_Warning(self):
        with Mesugaki(Warning):
            import warnings
            warnings.warn("警告测试", Warning)
    
    def test_DeprecationWarning(self):
        with Mesugaki(DeprecationWarning):
            import warnings
            warnings.warn("弃用警告测试", DeprecationWarning)
    
    def test_PendingDeprecationWarning(self):
        with Mesugaki(PendingDeprecationWarning):
            import warnings
            warnings.warn("即将弃用警告测试", PendingDeprecationWarning)
    
    def test_RuntimeWarning(self):
        with Mesugaki(RuntimeWarning):
            import warnings
            warnings.warn("运行时警告测试", RuntimeWarning)
    
    def test_SyntaxWarning(self):
        with Mesugaki(SyntaxWarning):
            import warnings
            warnings.warn("语法警告测试", SyntaxWarning)
    
    def test_UserWarning(self):
        with Mesugaki(UserWarning):
            import warnings
            warnings.warn("用户警告测试", UserWarning)
    
    def test_FutureWarning(self):
        with Mesugaki(FutureWarning):
            import warnings
            warnings.warn("未来警告测试", FutureWarning)
    
    def test_ImportWarning(self):
        with Mesugaki(ImportWarning):
            import warnings
            warnings.warn("导入警告测试", ImportWarning)
    
    def test_UnicodeWarning(self):
        with Mesugaki(UnicodeWarning):
            import warnings
            warnings.warn("Unicode警告测试", UnicodeWarning)
    
    def test_BytesWarning(self):
        with Mesugaki(BytesWarning):
            import warnings
            warnings.warn("字节警告测试", BytesWarning)
    
    def test_ResourceWarning(self):
        with Mesugaki(ResourceWarning):
            import warnings
            warnings.warn("资源警告测试", ResourceWarning)

if __name__ == '__main__':
    unittest.main()
