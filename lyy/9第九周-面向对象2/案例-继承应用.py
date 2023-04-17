"""
父类：计算正方形面积与周长，定义属性为边长
子类：计算长方体表面积和体积，重写父类的构造方法
"""
class Square_Father_zf(object):

    def __init__(self, length):
        self.length = length

    def perimeter(self):
        """正方形的周长"""
        p = self.length * 4
        return p

    def area(self):
        """面积"""
        a = self.length ** 2
        return a


class Square_Son_cf(Square_Father_zf):
    def __init__(self, length, kuan, gao):
        super().__init__(length)
        self.kuan = kuan
        self.gao = gao
    def perimeter(self):
        """长方形的表面积"""
        s = (self.length * self.kuan * 2) + (self.kuan * self.gao * 2)+(self.length * self.gao * 2)
        return s

    def area(self):
        """体积"""
        j = self.length * self.kuan * self.gao
        return j

# 正方形
g = Square_Father_zf(length=6)
print(g.perimeter())
print(g.area())
# 实例化对象，一个长方形
s = Square_Son_cf(length=10, kuan=5, gao=3)
print(s.perimeter())
print(s.area())


