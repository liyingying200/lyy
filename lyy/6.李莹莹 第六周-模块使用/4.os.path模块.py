"""
os.path:操作目录的模块
"""
import os
# 1.abspath:返回目录或文件的绝对路径
abs = os.path.abspath("ft.py")
print(abs)
# 2.exists():判断目录或文件是否存在，存在返回True
if os.path.exists("ft.py"):
    os.remove("ft.py")
else:
    print("不存在这个文件")
# 创建文件，文件不存在创建
if os.path.exists("news.txt"):
    print("已经存在")
else:
    open("news.txt","w",encoding="utf-8")
# 3.join():拼接路径与目录或文件名字，组成绝对路径
cwd = os.getcwd()
absur1 = os.path.join(cwd,"new.py")
print(absur1)
# 4.split():指定文件或目录进行切割，将名字切出来，结果放入元组中
res = os.path.split(cwd)
print(res)
# 5.splitext()：将文件的拓展名进行切割
res2 = os.path.splitext(r"C:\Users\大威天龙\Desktop\lyy\6.李莹莹 第六周-模块使用\news.txt")
print(res2)
# 6.basename():从路径中提取目录或文件名字
name = os.path.basename(cwd)
print(name)
# 7.dirname():从路径中提取文件的路径，不包括文件名字
name2 = os.path.dirname(cwd)
print(name2)
# 8.isdir():判断是否为路径
print(os.path.isdir("abc/ert/a"))
print(os.path.isdir(cwd))
# 9.isfile():判断是否为文件
print(os.path.isfile("new.txt"))
# 练习，将一个目录中所有的py文件进行统计，应该有多少
def countpy(path):
    pylist = []
    if os.path.isdir(path):
        allfile = os.listdir(path)
        for f in allfile:
            if os.path.isfile(f) and ".py" == os.path.splitext(f)[-1]:
                pylist.append(f)
            print(pylist)
        print(allfile)
    return len(pylist)
n = countpy(path=r"C:\Users\大威天龙\Desktop\lyy\6.李莹莹 第六周-模块使用")
print(n)