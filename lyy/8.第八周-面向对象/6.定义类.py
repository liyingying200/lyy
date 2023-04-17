# 定义一个类
# 类名：需要首字母大写,遵循大驼峰命名原则，多个单词命名时首字母都大写
class Person:
    pass
# 首字母大写是规范，不是必要要求
class dog:
    pass

# 创建学生类
class Student:
    pass
# 创建班级类
class Class:
    pass

# 创建人的对象，创建对象的过程叫实例化对象
zhangsan = Person()
# 创建学生
smc = Student()
# 查看类，查看对象
print(Student)      # <class '__main__.Student'>
print(smc)          # <__main__.Student object at 0x000001217CED0128>


class Boyfriend:
    pass

shitianyu = Boyfriend()
print(shitianyu)