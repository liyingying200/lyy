# 定义类，在外部添加属性
class Hero:
    pass
# 实例化对象
daji = Hero()
# 添加属性，通过对象添加属性
daji.name = "妲己"
daji.occ = "法师"
daji.hp = 4990
daji.mp = 800
daji.attact = 180
# 利用对象调用属性
print(f"{daji.name}:职业是{daji.occ},血量{daji.hp},魔法值{daji.mp},攻击力{daji.attact}")

# 2.定义类，添加类属性
class BoyFriend:
    # 定义类属性
    height = 188
    weiht = 140
    fule = "白"
    job = "甜品店老板"
    pay = 100000000
# 实例化对象，这个对象会带有类属性
bf1 = BoyFriend()
print(f"你的男朋友是{bf1.job},年薪{bf1.pay}")
bf2 = BoyFriend()
print(f"你的男朋友是{bf1.job},年薪{bf1.pay}")
# 通过类给类添加属性，这个属性会是类属性，所有实例化的对象都会有这个属性
BoyFriend.say = "I LOVE YOU"
bf4 = BoyFriend()
print(bf4.say)
print(bf1.say)
# 通过类调用属性
print(BoyFriend.height,BoyFriend.weiht)

# 2.通过对象添加属性,这个属性只属于这个对象，其他的对象没有，类也没有
huazai = BoyFriend()
huazai.sing = "会唱歌"
print(huazai.sing)
# print(bf1.sing)
# 类不能调用对象的属性
# print(BoyFriend.sing)
