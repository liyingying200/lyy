# 定义类时，一些属性在类的内容使用，在外部限制访问，称为私有属性
"""
类的内部属性和方法，类外调用属性和方法进行数据操作
当属性不行修改，就需要在创建属性时进行保护，在外部不能修改属性
__func__:首位双下划线表示特殊方法，系统定义的方法例如：__init__()
_name(半保护):单下划线开头的属性或方法表示保护类型的成员，只允许类本身与子类进行调用，对象可以调用修改
__name(私有属性）：双下划线开头属性或方法表示私有类型
"""
from tls import *
print(age)

class Cat:
    # 共有类属性
    name = "汤姆"
    # 保护属性
    _age = 16
    # 私有属性
    __job = "底下党"

    def __work(self):
        print("给党传递情报")

# 实例化一个对象
tang = Cat()
print(tang.name)
tang.name = "杰克"
print(tang.name)

# 访问被保护属性
print(tang._age)
print(Cat._age)

# 修改被保护属性
tang._age = 18
print(tang._age)

# 对象访问私有属性，报错
# print(tang.__job)

# 类访问私有属性，报错
# print(Cat.__job)

# 加入类名访问
ct = Cat()
# 对象._类名__私有属性  这种方式可以访问到私有属性
print("加入类名访问",ct._Cat__job)  # 这种方式叫强制访问

# 访问私有方法
# ct.__work()
# Cat.__work()
ct._Cat__work()
