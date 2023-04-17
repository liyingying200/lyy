# 定义变量
"""
变量：在程序运行过程中发生变化的量
表面理解：个这个常量起个名字，或贴上一个标签
变量实质：就是在程序运行过程中，定义的变量会被开辟一块存储空间，
将数据放进去，可以变量名调用里面的数据使用
 当变量数据值一样的时候，他们的ID地址是相同的

"""
# = :赋值符号，将666赋值给num
num = 666
# *：乘以
num = num * 2
print(num)
name = "李冰冰"
print(name)
mark = 9.96
print(mark, type(mark))
# id():带括号的叫函数，查看变量的内存地址
print(id(num))  # 1921852298672
nm = "李冰冰"
print(id(nm), id(name))
print(nm, name)

a = 89
a = a * 9
print(a)

# 选中内容，shift+tab键往左边移动，tab往右边移动



