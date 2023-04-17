"""
python内置的模块：os模块，re模块，time，datetime，random。。。
模块（modules):变量，函数，类，放入一个py文件中，可以让其他的文件调用；一个py文件叫脚本，可以单独运行使用

"""
# 1.导入自定义的模块；执行这句导入的代码，模块里面所有的程序执行一遍
import function_tools
""" 
使用模块的优点
1.不用重复的定义函数，可以重复使用定义好的函数，变量，类
2.避免命名冲突
"""
name = "李四"
sge = 88
phone = 12345678909
# 使用模块中的函数;调用方法：模块名.变量名   模块名.函数名
print(function_tools.name,function_tools.age,function_tools.phone)
print(function_tools.add(x=10,y=99))
function_tools.odd(23)
# 2.使用form...import...方式导入
# 这里导入的变量将上边的变量进行重新赋值
# from function_tools import  name, age,phone,add
from function_tools import *   # *代表模块所有的变量，函数，类
print(name,age,phone)
print(add(1,1))
print(Student.__name__)
# 3.导入后起别名
import function_tools as ft
print(ft.name,ft.age,ft.phone,ft.Student)
ft.odd(90)
print(function_tools.name)
# 4.导入Python的内置模块，导入多个模块，逗号隔开
import os,time,datetime,function_tools
print(os.name)
print(time.time()) # 时间戳
# 5.模块搜索
"""
1.自定义模块（优先使用）2.Python内置模块3.第三方模块（需要下载安装）
查找的顺序 1-当前目录下 2-到环境变量目录下查找 3-Python默认安装目录下查找
"""
import math  # 数学模块，里面数学相关的函数
# print(math.name)
import sys
print(sys.path)
