import unittest
#============================
from src.mesugaki import Mesugaki

class Mesugaki(Mesugaki):
    def __init__(self, exception):
        super().__init__()
        self.s_onlyException = exception.__name__

    def error(self, errorType, errorText):
        '''将错误信息重写'''
        if errorType not in self.d_table or errorType != self.s_onlyException:
            raise KeyError(f"没有犯 {self.s_onlyException} 错误？聪…聪明？才怪，还是笨蛋啦~")
        else:
            string = self.d_table[errorType](errorText)
        if self.b_original:
            #有显示原文的需求
            string += "\n" + errorText
        return string

class TestAddFunction(unittest.TestCase):
    #example
    def test_Exception(self):
        with Mesugaki(Exception):
            pass
    """
    def test_MemoryError(self):
        with Mesugaki() as baka:
            baka.only(MemoryError)
            10 ** 10 ** 10 ** 10 ** 10
    """
    def test_ZeroDivisionError(self):
        with Mesugaki(ZeroDivisionError):
            1/0

    def test_AttributeError(self):
        with Mesugaki(AttributeError):
            "a".test
  
if __name__ == '__main__':
    unittest.main()