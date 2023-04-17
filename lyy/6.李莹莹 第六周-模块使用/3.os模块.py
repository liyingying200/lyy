"""
so模块：处理系统的目录
"""
import os
# os里面的变量
# 1.name: 获取操作系统的名字，windows是nt，linux系统，Unix系统，Mac OS是posix
name = os.name
print(name)
# 2.linesep:获取系统的换行符；Window系统是“\r\n",linux路径分割符号是\
lp = os.linesep
print(lp)
# C:\Users\大威天龙\Desktop\lyy\6.李莹莹 第六周-模块使用\3.os模块.py
# 3.sep:获取系统路径的分割符号,window,linux 路径分割符号是 \
sep = os.sep
print(sep)

# os里面的函数
# 1.getcwd():获取当前工作环境的路径，类比linux的pwd命令
cwd = os.getcwd()
print(cwd)

# 2.mkdir():创建一个空目录，如果目录存在会报错
# os.mkdir("abc")
# os.mkdir(path=r"C:\Users\大威天龙\Desktop\lyy\6.李莹莹 第六周-模块使用\tools\空目录")

# 3.makedirs():创建多级目录，创建目录存在会报错
# os.makedirs("a/b/c")

# 4.chdir():切换当前工作环境目录
os.chdir(r"C:\Users\大威天龙\Desktop\lyy\1.第一周")
cwd1 = os.getcwd()
print(cwd1)
# os.mkdir("第一周的目录")
os.chdir(path=cwd)

# 5.rmdir():删除单个空目录，删除的目录如果找不到会报错
# os.rmdir("abc")

# 6.removedirs():删除多级目录，目录不存在会报错
# os.removedirs("a/b/c")

# 7.listdir():查看某个路径下边的文件和目录的信息，返回一个列表，每个元素是文件和目录名字
cwd2 = os.getcwd()
ld = os.listdir(path=cwd2)
print(ld)

# 8.walk():遍历目录树，返回一个元组，又三个元素，路径名，目录列表，文件列表
res = os.walk(r"C:\Users\大威天龙\Desktop\lyy\6.李莹莹 第六周-模块使用")
print(res)
# for r in res:
#     print(r)

# 9.temove():删除指定的文件，若不存在会报错
# os.remove("math.py")
# os.remove(r"C:\Users\大威天龙\Desktop\lyy\作业练习\__init__.py")

# 10.rename():重命名文件或目录，新名字如果存在会报错
# os.rename("猜拳游戏.py","自定义游戏.py")
# os.rename("自定义游戏.py","猜拳游戏.py")

# 11.stat():返回文件的系统相关的信息
res = os.stat("function_tools.py")
print(res)

# 12.copyfile():在shuil模块里的函数，复制文件
import shutil
shutil.copyfile("function_tools.py","ft.py")