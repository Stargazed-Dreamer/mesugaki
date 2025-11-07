# mesugaki

将Python异常处理的信息转为雌小鬼和傲娇口气~
纯Python实现，无第三方库
仅支持中文
## 注意
#### 本项目仅供娱乐，由于使报错复杂，不适合Python初学者使用
#### 由于实现方式并未触及底层虚拟机，在多进程、多线程等条件下可能无法保证子进程、子线程能应用本项目
#### 目前已囊括大部分Python内置异常类型，您可以考虑作出[贡献](#贡献)
## 安装
### 从whl安装
```bash   ”“bash   ”“bash”“bash
pip install mesugaki-1.3.0-py3-none-any.whlPIP安装mesugaki-1.3.0-py3-none-any.whlmesugaki-1.3.0-py3-none-any.whlPIP
```
### 从源码安装
```bash   ”“bash   ”“bash”“bash
git clone https://github.com/Stargazed-Dreamer/mesugaki
cd mesugaki
pip install .   PIP安装。
```
## 使用
### 1. 上下文管理器用法
```python   ”“python   ”“python”“python“蟒蛇” “蟒蛇” “蟒蛇” "蟒蛇
from mesugaki import Mesugakimesugaki的翻译结果
with Mesugaki():   与Mesugaki ():与Mesugaki (): Mesugaki()：
    1/0
```
示例输出：
```
杂~鱼🧡！让人家看看哥哥的蟒蛇怎么样了~
笨 蛋 ！ 蟒蛇都能写错~
才…才不会告诉你…是 "<stdin>" 的第 3 行中 <module> 出…出现的问题
    1/0
杂鱼~ 就连你的除数也是零吗~
```
### 2. 显示原始文件路径（此时支持IDE错误跳转）
```python   ”“python
from mesugaki import Mesugakimesugaki的翻译结果
Mesugaki.use_original_location_hint = TrueMesugaki。use_original_location_hint = True
with Mesugaki():   与Mesugaki ():与Mesugaki (): Mesugaki()：
    1/0
```
示例输出：
```
杂~鱼🧡！让人家看看哥哥的蟒蛇怎么样了~
笨 蛋 ！ 蟒蛇都能写错~
  File "<stdin>", line 3, in <module>文件“”，第3行，在
    1/0
杂鱼~ 就连你的除数也是零吗~
```
### 3. 全局快速启用
```python   ”“python
from mesugaki import alwaysMesugaki从mesugaki进口
# 启用全局钩子
1/0   # 这里的错误会被mesugaki处理
```
停止全局钩子：
```python   ”“python
from mesugaki import alwaysMesugaki从mesugaki进口

# 方法一：import stopMesugaki
from mesugaki import stopMesugaki从mesugaki进口停止mesugaki
# 方法二：调用stop方法
alwaysMesugaki.stop()
```
### 4.调试模式
```python   ”“python   ”“python”“python“蟒蛇” “蟒蛇” “蟒蛇” "蟒蛇
from mesugaki import alwaysMesugaki从mesugaki进口
Mesugaki.test_mode = TrueMesugaki。test_mode = TrueMesugaki。test_mode = TrueMesugaki。test_mode = TrueMesugaki。test_mode = TrueMesugaki。test_mode = TrueMesugaki。test_mode = TrueMesugaki。test_mode = True
1/0
```
示例输出：
```
杂~鱼🧡！让人家看看哥哥的蟒蛇怎么样了~
笨 蛋 ！ 蟒蛇都能写错~
  才…才不会告诉你…是 "<stdin>" 的第 3 行中 <module> 出…出现的问题
    1/0
杂鱼~ 就连你的除数也是零吗~

Original exception was:   最初的例外是：
Traceback (most recent call last):回溯（最近一次调用）：
  File "<stdin>", line 3, in <module>文件“”，第3行，在
    1/0
ZeroDivisionError: division by zeroZeroDivisionError：除零错误
```
## 贡献
欢迎贡献！目前需要改进的地方：
1. 添加更多细分异常类型的处理
2. 优化错误信息解析
3. 添加多语言支持
##### 添加新的异常处理
1. 在 `mesugaki/handlers` 目录下创建新文件或修改现有文件
2. 使用 `register_exception` 装饰器注册处理函数：
   ```python   ”“python   ”“python”“python“蟒蛇” “蟒蛇” “蟒蛇” "蟒蛇
   from mesugaki.data import register_exception从mesugaki。数据导入register_exception
   @register_exception("YourException")@register_exception(“YourException”)@register_exception(“YourException”)@register_exception(“YourException”)
   def handle_your_exception(text):def handle_your_exception(文本):Def handle_your_exception(text): Def handle_your_exception（中文）：
       return "你的自定义错误信息"
   ```
3. 在 `test_main.py` 中添加测试用例
### 运行测试
```bash   ”“bash   ”“bash”“bash
python -m unittest test_main.pyPython -m unittest test_main.pyPython -m unittest test_main。ppython -m unittest test_main.py
```
## 许可证
根据 [Apache 2.0 license](https://github.com/gaogaotiantian/viztracer/blob/master/LICENSE) 的条款分发
## 其它
灵感来源于 [此视频](https://www.bilibili.com/video/BV1gC4y1P7t3)

另贴上评论区另一位大佬的 [项目](https://github.com/Flotiarenor/Python-3.10.13)，修改的是底层CPython，能够规避多进程不兼容的问题
