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
            "MemoryError": self.MemoryError,
            "ZeroDivisionError": self.ZeroDivisionError,
        }
        self.compile_AttributeError = re.compile(".*'(.*)' object has no attribute '(.*)'")

    def AttributeError(self, text):
        former, latter = self.compile_AttributeError.match(text).groups()
        return f'笨 蛋 ！ 你的(ー`´ー)对象 "{former}" 可没有成员 "{latter}"… 不信？你自己去问人家~'

    def MemoryError(self, text):
        return "笨 蛋 ！ 都溢出来了~"

    def ZeroDivisionError(self, text):
        return "杂鱼~ 除数就和你抽卡的出货率一样呢~"