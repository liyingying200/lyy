"""
类属性，实例属性，实例方法，类方法，静态方法
"""
class Math():
    # 类属性:直接在类中定义，静态属性（不会根据对象进行改变），类和实例对象可以进行访问
    length = 100
    width = 80
    def __init__(self,name,shape):
        # 构造方法，添加实例属性
        self.name = name
        self.shape = shape

    def func_one(self,num):
        # 实例方法，有参数self，输入
        if num % 2 == 0 :
            return "偶像"
        else:
            return "奇数"
    @classmethod      # @classmethod:装饰器，将实例方法转化为类方法
    def cls_func(cls):
        # cls参数：类似self参数，cls指的是本身，self是实例对象本身
        # cls只能使用类属性，不能使用实例属性
        print("这个是类方法，类：",cls.length)
    @staticmethod    # 将实例方法变成静态方法，就是类似普通函数
    def fun():
        # 静态方法无法使用类属性和实例属性
        print("这个就是普通函数，定义在类中")
if __name__ == '__main__':
    # 1.访问修改类属性
    m = Math(name="数学类",shape="四边形")
    print(m.length,Math.length)  # 对象与类名进行访问类属性
    m.length = 10       # 对象修改类属性
    Math.width = 8        # 类修改类属性
    print(m.length,m.width)
    # 2.访问修改实例属性
    a = Math(name = "计算类", shape="长方形")
    print(a.name,a.shape) # 实例对象可以访问私有属性外其他属性，都可以访问
    a.name = "科学类"  # 实例对象可以修改私有属性外其他属性，都可以修改
    print(a.name)
    # print(Math.name)   # 类不能访问，修改实例属性，实例属性在实例化才会产生
    # 3.调用实例方法
    t = Math(name="判断奇偶",shape = "无")
    t.func_one(num=90)  # 通过实例对象调用实例方法
    Math.func_one(self = t,num = 80) # 类名调用实例方法，必须给self传入参数，所以需要提前实例化对象当做实参传入
    # 4.调用类方法
    Math.cls_func()   # 类方法可以使用类直接调用，cls参数就是类自己，自动传入
    h = Math(name="类方法",shape="无")
    h.cls_func()   # 类实例化的对象可以调用类方法
    # 5.调用静态方法
    Math.fun() # 可以使用类调用
    mh = Math(name="静态方法",shape="无")
    mh.fun()   # 可以使用对象调用