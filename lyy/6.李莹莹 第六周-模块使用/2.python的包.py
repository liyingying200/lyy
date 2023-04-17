"""
包：就是将一堆模块放入目录下边，这个目录含义文件 __init__.py
"""
# 1.创建一个tools的包，包含文件叫__init__.py
# 在导入包的时候，init文件里面内容第一执行，初始化文件
import tools.function_tools
tools.function_tools.odd(number=20)
# 2.直接导入包里面的模块；模块命名冲突时起一个别名
from tools import  function_tools as ft
print(ft.name)
import function_tools
print(function_tools.name)
print(ft.name)

# 3.导入其他模块
"""
自定义模块，内置模块，第三方安装
"""
import random   # 随机数
print(random.randint(1,10))
caiq = ["石头","剪刀","布"]
# we = input("输入：")
print(random.choices(caiq)[0])
"""
标准库：官方认可的库
sys:模块与Python解释器和环境操作相关
os：操作我们当前操作系统的目录
time：操作时间，处理时间格式
datetime：操作日期
calendar：操作日期
urllib：请求网页获取数据
json：处理json数据，序列化，反序列
re：正则表达式，精准匹配字符串使用
math：与数学运算有关，数学相关的函数
shutil:用于高级文件操作，复制，移动，重命名
tkinter:用于GUI编程模块
random:生成随机数
"""
# 第三方模块下载安装
"""
1.第一种安装方式，pop install 模块名字 (requests, numpy, pymysql)
默认从官方网站下载安装
pip install 模块名 -i https://pypi.douban.com/simple/
2.第二种安装，使用pycharm安装功能
"""
# import pymysql
