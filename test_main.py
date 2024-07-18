import unittest
#============================
from src.mesugaki import Mesugaki

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

class Test(unittest.TestCase):
    #example
    def test_Exception(self):
        with Mesugaki(Exception):
            raise Exception("example")
    """
    def test_MemoryError(self):
        with Mesugaki(MemoryError):
            10 ** 10 ** 10 ** 10 ** 10
    """
    def test_ZeroDivisionError(self):
        with Mesugaki(ZeroDivisionError):
            1/0

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
  
if __name__ == '__main__':
    unittest.main()