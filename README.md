# mesugaki
将python异常处理的信息转为雌小鬼和傲娇口气\~

纯python实现，无第三方库

仅支持中文
## 注意
#### 本项目仅供娱乐，由于使报错复杂，不适合初学者使用
#### 由于实现方式并未触及底层虚拟机，在多进程、多线程等条件下可能无法保证子进程、子线程能应用本项目
#### 目前仅囊括了AttributeError、Exception、MemoryError、ZeroDivisionError以及TypeError的一部分信息，更多替换尚未完工，您可以考虑作出[贡献](https://github.com/StaryDreamer/mesugaki/blob/main/README.md#%E8%B4%A1%E7%8C%AE)
## 安装
目前没有上传PyPI，请手动下载

或使用release进行安装

## 使用
有且仅有上下文管理器的用法
```python
from mesugaki import Mesugaki

with Mesugaki():
    ...
```
示例：
```python
from mesugaki import Mesugaki

with Mesugaki():
    1/0
```
输出：
~~~
杂~鱼🧡！让人家看看哥哥的蟒蛇怎么样了~
笨 蛋 ！ 蟒蛇都能写错~
才…才不会告诉你…是 "<temp>" 的第 4 行中 <module> 出…出现的问题
    1/0
    ~^~
杂鱼~ 就连你的除数也是零吗~
~~~

## 贡献
由于作者过懒，本项目有大量修改空间

有不少异常文本有待替换

想要加入，你至少需要修改`mesugaki\data.py`文件

如果愿意，你还可以同步添加一个测试到`test_main.py`

#### 但请注意，添加的各个异常处理方法、键等，一定要按照字母表的顺序排列

### data.py修改

*以下操作默认在`mesugaki\data.py`中进行*

1. 准备
   1. 查看`ExceptionHandler.d_table`
   2. 综合各类异常，参见`doc\所有异常.txt`
2. 增加
   1. 增加一个对应异常名称的方法，可结合正则表达式re进行字符串寻找。
   2. 若需要结合正则表达式进行字符串寻找，请添加一个名称类似`compile_Exception_1`的`re.compile`对象，再到方法中使用它。
      使用re推荐搭配python官方提供的[re测试工具](https://github.com/python/cpython/tree/3.11/Tools/demo/redemo.py)进行测试
   3. 在`ExceptionHandler.d_table`增加一个对应项
3. 完成

这样就可以pull request了！

如果你还有兴趣，可以协助增加一个测试，操作见下方

### test_main.py修改

见文件中的example即可

## 许可证

根据[Apache 2.0 license](https://github.com/gaogaotiantian/viztracer/blob/master/LICENSE)的条款分发

## 感谢
灵感来源于[此视频](https://www.bilibili.com/video/BV1gC4y1P7t3)

另贴上评论区另一位大佬的[项目](https://github.com/Flotiarenor/Python-3.10.13)，修改的是底层CPython，大家也可以参观学习~
