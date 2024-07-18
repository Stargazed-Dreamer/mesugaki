import traceback
import sys

def print_error_location():
    try:
        # 这里尝试执行可能引发错误的代码
        1 / 0
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # 提取堆栈跟踪中的帧
        frames = traceback.extract_tb(exc_traceback)
        # 遍历帧，打印出每个错误位置的文件及行信息
        #for frame in frames:
        #    filename, line, func, text = frame
        #    print(f'  File "{filename}", Line {line}, in {func}')
        #    print(f"    {text}")

#print_error_location()

def extract_error_indicator():
    try:
        # 尝试执行可能引发错误的代码
        1 / 0
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # 格式化堆栈跟踪
        formatted_traceback = traceback.format_exception(exc_type, exc_value, exc_traceback)
        # 遍历堆栈跟踪中的每一行
        for line in formatted_traceback:
            print(line, end = "")

#extract_error_indicator()