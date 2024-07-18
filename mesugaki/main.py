#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#============================
#个人命名习惯：
#对于非callable对象，采用小驼峰，且有时在名称前用下划线标注类型。如：s_a = "xxx"; i_a = 1
#对于callable对象，函数采用小驼峰、名称较长体现功能，类采用大驼峰、名称较短表示大的功能分区
#函数有时会在前面用下划线区分属于哪个功能区
#============================
import re
from sys import exc_info
from traceback import format_exception
#============================
from .data import ExceptionHandler, heart
#============================
class Mesugaki:
    def __init__(self):
        self.d_table = ExceptionHandler().d_table
        self.b_original = False

    def __enter__(self):
        '''上下文管理器进入时自动调用'''
        print(f"杂~鱼{heart(1)}！让人家看看哥哥的蟒蛇怎么样了~")
        # 可以返回不同的对象，但通常返回self
        return self
  
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''上下文管理器退出时自动调用'''
        # exc_type, exc_val, exc_tb 分别代表异常类型、异常值和追踪信息
        if exc_type is not None:
            exc_type, exc_value, exc_traceback = exc_info()
            # 格式化堆栈跟踪
            l_traceback = format_exception(exc_type, exc_value, exc_traceback)
            #初始化
            self.output = ""
            self.compile_fileLine = re.compile(' *File "(.+)", line ([0-9]+), in (.+)')
            #堆栈字符串列表预处理
            #去掉换行
            l_error = []
            for string in l_traceback:
                l_lines = string.split("\n")
                if "" in l_lines:
                    l_lines.remove("")
                l_error += l_lines
            #第一句应当是这个
            assert l_error.pop(0) == "Traceback (most recent call last):"
            #去掉错误类别及提示
            originalExceptionText = l_error.pop(-1)
            #乐
            self.add(f"笨 蛋 ！ 蟒蛇都能写错~")
            #进入堆栈处理循环
            self.loop_main(l_error)
            #替换错误类别及提示
            exceptionText = self.error(exc_type.__name__, str(exc_value))
            if self.b_original:
                self.add(originalExceptionText)
            else:
                self.add(exceptionText)
            print(self.output)
        else:
            print(f"哼╯^╰  也……也就勉勉强强会玩蟒蛇嘛{heart(3)}~\n")
        # 如果为False，则异常会被正常抛出；如果为True，则异常会被忽略
        return True

    def error(self, errorType, errorText):
        '''将错误信息重写'''
        if errorType not in self.d_table:
            string = f"哎呀~ 人家才不是连这个错误都不认识呢~\n{errorType}: {errorText}"
        else:
            string = self.d_table[errorType](errorText)
        if self.b_original:
            #有显示原文的需求
            string += "\n" + errorText
        return string

    def add(self, string=None):
        '''向异常捕获输出增加字符串'''
        if string is None:
            print(f"笨 蛋 ！ 你还没决定要把什么插进来呢{heart()}~")
            return
        try:
            #核心就这一行
            self.output += string + "\n"
        except AttributeError:
            print(f"杂鱼~ 还想偷偷插进来{heart()}~")

    def loop_main(self, l_error):
        '''异常堆栈处理循环，替换所有文件信息行'''
        while l_error:
            line = l_error.pop(0)
            result = self.compile_fileLine.match(line)
            if result is None:
                self.add(line)
            else:
                file, line, func = result.groups()
                string = f'才…才不会告诉你…是 "{file}" 的第 {line} 行中 {func} 出…出现的问题'
                self.add(string)

if __name__ == '__main__':
    # 使用with语句测试上下文管理器
    with Mesugaki():
        # 可以在这里引发异常来测试__exit__方法中的异常处理
        #raise Exception("Just testing")
        1/0
        #pass