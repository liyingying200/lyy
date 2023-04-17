class Dog(object):
    # 所有魔法方法来自object（基类
    # 方法前后双下划线，是Python定义的魔法方法
    def __init__(self,name):
        # 实例对象调用构造方法
        self.name = name
        print("构造方法被调用，创建实例：%s"% self.name)

    def __del__(self):
        print("在删除对象，调用析构函数")

    def __add__(self, other):
        # 实现实例的加法运算，字符串加法就是拼接字符串，数字的加法是数学运算，列表的加法是合并列表...
        return 9527

    # def __sub__(self, other):  实现减法运算
    # def __mul__(self, other):   实现乘法运算
    # def __matmul__(self, other):  实现除法运算

    def __len__(self):
        # len():计算实例对象的长度返回值
        count = 0
        for i in self.name:
            count += 1
        return count

    # def __lt__(self, other):  小于<
    # def __le__(self, other):  小于等于<=
    # def __eq__(self, other):  等于 ==
    # def __ne__(self, other):  不等于！=
    # def __gt__(self, other):  大于 >
    # def __ge__(self, other):  大于等于 >=

    def __bool__(self):
        # 在使用布尔值转换实例对象，返回的布尔值
        return True

    def __str__(self):
        return "是条狗"

if __name__ == '__main__':
    # 实例化
    d = Dog(name="多多多多多多")
    m = Dog(name="毛毛")
    print(d + m)
    print(len(d))
    print(bool(d))
    print(str(d))
