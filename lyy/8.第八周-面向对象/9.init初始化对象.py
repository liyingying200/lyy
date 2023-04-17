# 定义类
class Hero:
    # 类属性定义是固定的值，只能通过实例化后再修改
    # 所有的对象实例化得到的属性都一样
    print("类属性被执行")   # 定义类被执行，这里的类属性会被执行
    def __init__(self):
        """__init__(),方法叫魔法方法，是自定义自带的，来自基类
        在实例化类的时候，会首先调用这个方法，因此我们可以在这里定义属性"""
        print("这个init方法被调用")
# 实例化对象
xiaoqiao = Hero()

class Dog():

    def __init__(self,name,age,breed):      # 初始化函数，实例化对象被自动调用，进行传参
        # self:只对对象本身，self.name是对象属性
        self.name = name
        self.age = age
        self.breed = breed
# 实例化属性，构造一个对象
zaizai = Dog(name= "崽崽",age=3,breed="中华田园犬")
print(zaizai.name,zaizai.age,zaizai.breed)

# 再实例化一个
wkeke = Dog(name="石子",age=5,breed="德牧")
print(wkeke.name,wkeke.age,wkeke.breed)

# 练习: 使用init实例化一个班级类, 通过这个班级类构造出不同专业的班级, 定义方法进行上课

class cl():

    def __init__(self,specialized,num,teacher):
        self.specialized = specialized
        self.num = num
        self.teacher = teacher

    def time(self):
        print("人工智能班：第一二节，大数据班：第三四节，电商班：第七八节")
    def site(self):
        print("人工智能班：206教室，大数据班：207教室，电商班：204教室")

cl1 = cl(specialized= "人工智能班",num=40,teacher="zgs")
cl2 = cl(specialized="大数据班",num=43,teacher="yjy")
cl3 = cl(specialized="电商班",num=41,teacher="xy")

print(cl1.specialized,cl1.num,cl1.teacher)
print(cl2.specialized,cl2.num,cl2.teacher)
print(cl3.specialized,cl3.num,cl3.teacher)

cl1.time()
cl1.site()
