class Square():
    """计算正方形的周长和面积"""
    def __init__(self,length):
        self.length = length

    def zc (self):
        """计算周长的方法"""
        p = self.length * 4
        return p
    def area(self):
        """计算面积的方法"""
        a = self.length ** 2
        return a

# 实例化对象，一个正方形
s = Square(length=10)
print(s.zc())  # 调用计算周长的方法
print(s.area()) # 调用计算面积的方法

# 练习： 升级上边的案例 ，定义一个类计算出长方形的周长和面积
class Changfangxing():
    def __init__(self,chang,kuan):
        self.chang = chang
        self.kuan = kuan

    def zhouchang(self):
        r = self.kuan * 2 + self.chang * 2
        return r
    def mianji(self):
        n = self.chang * self.kuan
        return n

q = Changfangxing(chang=3,kuan=1)
print(q.zhouchang())
print(q.mianji())

