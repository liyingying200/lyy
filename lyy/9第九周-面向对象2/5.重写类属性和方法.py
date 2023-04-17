# 继承: 子类继承父类的属性和方法, 私有属性不能继承, 子类可以拥有自己的属性和方法, 子类也可以重写父类的属性和方法
# 继承是为了代码复用
class A(object):
    height = 80
    width = 60
    length = 60

    def volume(self):
        """计算体积"""
        s = self.length * self.width
        return s * self.height

class B(A):
    # 新的类需要修改属性, 继承过程中叫重写属性
    height = 60     # 子类定义的属性与父类重名, 则子类的属性会覆盖父类的属性, 这是重写
    tp = "木头"

    def volume(self):
        # 子类的方法与父类重名, 子类覆盖父类的方法, 叫做方法重写
        return self.height ** 3
# 实例化对象
b = B()
print(b.height, b.width, b.length)
# 调用方法.
res = b.volume()
print(res)
# 练习: 定义父类, 计算三角形, 两个属性, 底边, 高度; 定义方法, 计算三角形的面积; 定义子类继承父类, 子类是正三角形, 只给边长, 重写继承的底边, 高度属性为None, 重写计算面积方法.
import math
class F(object):
    bottom_edge = 10
    height = 8
    def v(self):
        return  self.bottom_edge * self.height * 0.5
class S(F):
    bottom_edge = None
    height = None
    edge = 6
    def v(self):
        height = math.sqrt(self.edge ** 2 - (0.5*self.edge) ** 2)
        return  self.edge * height * 0.5

s = S()
print(f"三角形面积: {s.v():.2f}")