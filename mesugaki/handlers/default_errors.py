from mesugaki.data import register_exception
import re

@register_exception("BaseException")
def handle_base_exception(text: str):
    return f"哼！连基础异常都搞不定吗杂鱼~ {text}"

@register_exception("SystemExit")
def handle_system_exit(text: str):
    return "笨蛋！想逃跑吗~ 人家才不会让你走呢~"

@register_exception("KeyboardInterrupt")
def handle_keyboard_interrupt(text: str):
    return "杂鱼~ 按Ctrl+C是想中断什么呀~ 是不是受不了人家了~"

@register_exception("GeneratorExit")
def handle_generator_exit(text: str):
    return "哼！生成器都关了，人家也要关门了~"

@register_exception("Exception")
def handle_exception(text: str):
    return "哼！基本错误都能犯 杂鱼~"

@register_exception("StopIteration")
def handle_stop_iteration(text: str):
    return "笨蛋！已经没有东西可以给你了啦~ 再要人家就生气了！"

@register_exception("StopAsyncIteration")
def handle_stop_async_iteration(text: str):
    return "杂鱼~ 异步迭代也空了哦~ 人家什么都给不出了啦~"

@register_exception("ArithmeticError")
def handle_arithmetic_error(text: str):
    return f"笨蛋！算术都算不好吗~ {text}"

@register_exception("FloatingPointError")
def handle_floating_point_error(text: str):
    return "杂鱼~ 浮点数都算不准，真没用呢~"

@register_exception("OverflowError")
def handle_overflow_error(text: str):
    return "笨蛋！太大了啦~ 人家装不下这么大的数啦~"

@register_exception("ZeroDivisionError")
def handle_zero_division_error(text: str):
    return "杂鱼~ 就连你的除数也是零吗~"

@register_exception("AssertionError")
def handle_assertion_error(text: str):
    return f"哼！断言都失败了，真是个杂鱼~ {text}"

@register_exception("AttributeError")
def handle_attribute_error(text: str):
    compile_AttributeError_1 = re.compile(".*'(.*)' object has no attribute '(.*)'")
    
    if result := compile_AttributeError_1.match(text):
        former, latter = result.groups()
        return f'笨蛋！ 你的对象 "{former}" 可没有成员 "{latter}" 喔~  不信？你自己去问人家(ー`´ー)'
    
    return None

@register_exception("BufferError")
def handle_buffer_error(text: str):
    return "杂鱼~ 缓冲区都搞不定，真没用呢~"

@register_exception("EOFError")
def handle_eof_error(text: str):
    return "笨蛋！到头了啦~ 人家已经没有东西给你了~"

@register_exception("ImportError")
def handle_import_error(text: str):
    return f"哼！连模块都导不进来，杂鱼~ {text}"

@register_exception("ModuleNotFoundError")
def handle_module_not_found_error(text: str):
    compile_ModuleNotFound = re.compile(r"No module named '(.*)'")
    if result := compile_ModuleNotFound.match(text):
        module = result.groups()[0]
        return f'笨蛋！人家才没有 "{module}" 这种东西呢~ 快去找别家啦~'
    return f"杂鱼~ 模块都找不到，真没用呢~"

@register_exception("LookupError")
def handle_lookup_error(text: str):
    return f"哼！查找都找不到，杂鱼~ {text}"

@register_exception("IndexError")
def handle_index_error(text: str):
    return "笨蛋！太大了啦~ 人家那里没有那么深的位置给你插呢~"

@register_exception("KeyError")
def handle_key_error(text: str):
    match = re.search(r"'(.+)'", text)
    key = match.group(1) if match else "某个东西"
    return f"哼！{key}？人家才没有这种东西呢~"

@register_exception("MemoryError")
def handle_memory_error(text: str):
    return "笨蛋！ 都溢出来了~"

@register_exception("NameError")
def handle_name_error(text: str):
    compile_NameError = re.compile(r"name '(.*)' is not defined")
    if result := compile_NameError.match(text):
        name = result.groups()[0]
        return f'杂鱼~ 人家才不认识叫 "{name}" 的家伙呢~'
    return "笨蛋！名字都搞错，真是个杂鱼~"

@register_exception("UnboundLocalError")
def handle_unbound_local_error(text: str):
    compile_UnboundLocal = re.compile(r"local variable '(.*)' referenced before assignment")
    if result := compile_UnboundLocal.match(text):
        var = result.groups()[0]
        return f'笨蛋！"{var}" 还没准备好就被你用了，变态！'
    return "杂鱼~ 局部变量都搞不定，真没用呢~"

@register_exception("OSError")
def handle_os_error(text: str):
    return f"哼！系统都搞不定，杂鱼~ {text}"

@register_exception("BlockingIOError")
def handle_blocking_io_error(text: str):
    return "笨蛋！阻塞了啦~ 人家现在不想动呢~"

@register_exception("ChildProcessError")
def handle_child_process_error(text: str):
    return "杂鱼~ 子进程都搞不定，真没用呢~"

@register_exception("ConnectionError")
def handle_connection_error(text: str):
    return f"哼！连接都连不上，杂鱼~ {text}"

@register_exception("BrokenPipeError")
def handle_broken_pipe_error(text: str):
    return "笨蛋！管道都破了，人家不干了啦~"

@register_exception("ConnectionAbortedError")
def handle_connection_aborted_error(text: str):
    return "杂鱼~ 连接被中止了，人家不要你了~"

@register_exception("ConnectionRefusedError")
def handle_connection_refused_error(text: str):
    return "笨蛋！人家拒绝和你连接啦~ 不要碰我！"

@register_exception("ConnectionResetError")
def handle_connection_reset_error(text: str):
    return "杂鱼~ 连接被重置了，人家要重新开始~"

@register_exception("FileExistsError")
def handle_file_exists_error(text: str):
    compile_FileExists = re.compile(r".*'(.*)'")
    if result := compile_FileExists.search(text):
        path = result.groups()[0]
        return f'笨蛋！"{path}" 已经被人家占有了啦~ 不许再插了！'
    return "杂鱼~ 文件已经存在了，真没用呢~"

@register_exception("FileNotFoundError")
def handle_file_not_found_error(text: str):
    compile_FileNotFound = re.compile(r".*'(.*)'")
    if result := compile_FileNotFound.search(text):
        path = result.groups()[0]
        return f'哼！人家才没有 "{path}" 这种东西呢~ 快去找别家啦~'
    return "笨蛋！文件都找不到，真是个杂鱼~"

@register_exception("InterruptedError")
def handle_interrupted_error(text: str):
    return "杂鱼~ 被中断了啦~ 人家正舒服呢~"

@register_exception("IsADirectoryError")
def handle_is_a_directory_error(text: str):
    return "笨蛋！那是目录啦~ 不许在里面乱插东西！"

@register_exception("NotADirectoryError")
def handle_not_a_directory_error(text: str):
    return "杂鱼~ 那不是目录啦~ 人家不要进去！"

@register_exception("PermissionError")
def handle_permission_error(text: str):
    return "哼！人家才不给你权限呢~ 杂鱼~"

@register_exception("ProcessLookupError")
def handle_process_lookup_error(text: str):
    return "笨蛋！进程都找不到，真没用呢~"

@register_exception("TimeoutError")
def handle_timeout_error(text: str):
    return "杂鱼~ 超时了啦~ 人家等不及了~"

@register_exception("ReferenceError")
def handle_reference_error(text: str):
    return "笨蛋！引用都搞错了，人家不要你了~"

@register_exception("RuntimeError")
def handle_runtime_error(text: str):
    return f"哼！运行时都出错，杂鱼~ {text}"

@register_exception("NotImplementedError")
def handle_not_implemented_error(text: str):
    return "笨蛋！人家还没准备好呢~ 不许碰那里！"

@register_exception("RecursionError")
def handle_recursion_error(text: str):
    return "杂鱼~ 太深了啦~ 人家受不了了~"

@register_exception("SyntaxError")
def handle_syntax_error(text: str):
    return f"笨蛋！语法都写错，真是个杂鱼~ {text}"

@register_exception("IndentationError")
def handle_indentation_error(text: str):
    return "杂鱼~ 缩进都搞不对，真没用呢~"

@register_exception("TabError")
def handle_tab_error(text: str):
    return "笨蛋！Tab和空格混用了，人家不喜欢~"

@register_exception("SystemError")
def handle_system_error(text: str):
    return f"哼！系统都出错了，杂鱼~ {text}"

@register_exception("TypeError")
def handle_type_error(text: str):
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

@register_exception("ValueError")
def handle_value_error(text: str):
    return f"哼！值都搞错了，杂鱼~ {text}"

@register_exception("UnicodeError")
def handle_unicode_error(text: str):
    return f"笨蛋！Unicode都搞不定，真没用呢~ {text}"

@register_exception("UnicodeDecodeError")
def handle_unicode_decode_error(text: str):
    compile_UnicodeDecode = re.compile(r"'(.*)' codec can't decode byte (0x[0-9a-f]+) in position ([0-9]+): (.*)")
    if result := compile_UnicodeDecode.match(text):
        codec, byte, pos, reason = result.groups()
        return f'杂鱼~ "{codec}" 解码器看不懂位置 {pos} 的 {byte} 呢~ {reason}'
    return "笨蛋！Unicode解码都搞不定，真是个杂鱼~"

@register_exception("UnicodeEncodeError")
def handle_unicode_encode_error(text: str):
    compile_UnicodeEncode = re.compile(r"'(.*)' codec can't encode character '(.*)' in position ([0-9]+): (.*)")
    if result := compile_UnicodeEncode.match(text):
        codec, char, pos, reason = result.groups()
        return f'杂鱼~ "{codec}" 编码器不喜欢位置 {pos} 的 "{char}" 呢~ {reason}'
    return "笨蛋！Unicode编码都搞不定，真没用呢~"

@register_exception("UnicodeTranslateError")
def handle_unicode_translate_error(text: str):
    return "杂鱼~ Unicode转码都搞不定，真是个杂鱼~"

@register_exception("Warning")
def handle_warning(text: str):
    return f"哼！警告都看不懂，杂鱼~ {text}"

@register_exception("DeprecationWarning")
def handle_deprecation_warning(text: str):
    return "笨蛋！这个已经过时了啦~ 人家不要旧的~"

@register_exception("PendingDeprecationWarning")
def handle_pending_deprecation_warning(text: str):
    return "杂鱼~ 这个快要过时了，快换新的吧~"

@register_exception("RuntimeWarning")
def handle_runtime_warning(text: str):
    return f"哼！运行时警告，杂鱼~ {text}"

@register_exception("SyntaxWarning")
def handle_syntax_warning(text: str):
    return "笨蛋！语法都有问题，真没用呢~"

@register_exception("UserWarning")
def handle_user_warning(text: str):
    return f"杂鱼~ 用户警告，听不懂呢~ {text}"

@register_exception("FutureWarning")
def handle_future_warning(text: str):
    return "笨蛋！这个在未来会变的，人家不喜欢~"

@register_exception("ImportWarning")
def handle_import_warning(text: str):
    return "杂鱼~ 导入警告，真没用呢~"

@register_exception("UnicodeWarning")
def handle_unicode_warning(text: str):
    return "笨蛋！Unicode警告，人家不懂啦~"

@register_exception("BytesWarning")
def handle_bytes_warning(text: str):
    return "杂鱼~ 字节警告，真是个杂鱼~"

@register_exception("ResourceWarning")
def handle_resource_warning(text: str):
    return f"哼！资源警告，杂鱼~ {text}"
