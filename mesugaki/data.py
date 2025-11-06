#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#============================
#个人命名习惯：
#对于非callable对象，采用小驼峰，且有时在名称前用下划线标注类型。如：s_a = "xxx"; i_a = 1
#对于callable对象，函数采用小驼峰、名称较长体现功能，类采用大驼峰、名称较短表示大的功能分区
#函数有时会在前面用下划线区分属于哪个功能区
#============================
import re
from hashlib import sha512
from time import time

s_hearts = "❤🧡💛💚💙💜"

def heart(index=None):
    '''在爱心表里随机或者指定一个爱心返回'''
    if index is None:
        seed = time()
        index = int(sha512(str(seed).encode('utf-8')).hexdigest(), base=16) % len(s_hearts)
    return s_hearts[index]

class ExceptionHandler:
    def __init__(self):
        self.d_table = {
            "AttributeError": self.AttributeError,
            "Exception": self.Exception,
            "MemoryError": self.MemoryError,
            "TypeError": self.TypeError,
            "ZeroDivisionError": self.ZeroDivisionError,
        }

    def AttributeError(self, text):
        compile_AttributeError_1 = re.compile(".*'(.*)' object has no attribute '(.*)'")

        if result := compile_AttributeError_1.match(text):
            former, latter = result.groups()
            return f'笨蛋！ 你的对象 "{former}" 可没有成员 "{latter}" 喔~  不信？你自己去问人家(ー`´ー)'

        return None

    def Exception(self, text):
        return None

    def MemoryError(self, text):
        return "笨蛋！ 都溢出来了~"

    def TypeError(self, text):
        compile_TypeError_1 = re.compile(
            "(.*) takes ([0-9]+) positional argument but ([0-9]+) (?:were|was) given"
            )
        compile_TypeError_2 = re.compile(
            "(.*) missing ([0-9]+) required positional (?:arguments|argument): (?:'(.*)')+ (?:and '(.*)')?"
            )

        if result := compile_TypeError_1.match(text):
            name, num_former, num_latter = result.groups()
            return f'笨蛋！ {name} 已经塞…塞不下了啦！只接受 {num_former} 个参数的它被你传入了 {num_latter} 个，变…变态！'

        elif result := compile_TypeError_2.match(text):
            name, num, *args = result.groups()
            s_args = " ".join([f'"{string}"' for string in args])
            return f'笨蛋！ {name} 感到空虚！现在还想要 {num} 个参数：{s_args}  好…好想要…'

        return None

    def ZeroDivisionError(self, text):
        return "杂鱼~ 就连你的除数也是零吗~"