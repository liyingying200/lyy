"""
random模块：生成随机数，做随机选择使用
"""
import  random
# 1.randint(a,b):产生一个[a，b]的随机整数
n = random.randint(1,9)
print(n)
# 2.random():产生一个[0,1)之间的一个随机浮点数
f = random.random()
print(f)
# 3.randrange(strt,stop,step):在[start,stop]之间以step步长产生一个随机数
res = random.randrange(0,10,2)    # 相当于在[0,2,4,6,8]
res1 = random.randrange(1,10,2)
print(res)
print(res1)
# 4.sample(list,k):在序列中随机取出k个元素，以列表形式返回
list1 = random.sample([1,2,3,4,5,6,7],k = 2)
print(list1)
# 5.seed():改变随机生成器的种子，默认的参数是系统的时间
import  time
print(time.time())     # 时间戳
# random.seed(0)
print(random.randint(1,9))
for i in range(10):
    print(random.randint(1,9))
# 6.shuffle():打乱序列中的元素
card = [c for c in range(1,11)]
card.extend(["j","q","k"])
print(card)
random.shuffle(card)
print(card)
# 7.uniform(a,b):在[a,b]范围内产生随机浮点数
ff = random.uniform(1.13,2.777)
print(ff)
# 8.choice():从序列表随机选取一个元素返回
y = random.choices(["石头","剪刀","布"])
print(y)
# 9.choices(sep,k):从序列中随机抽取多个元素放入列表返回
list2 = random.choices(list(range(10)),k = 2)
print(list2)
# 10.getrandbits(k):产生一个比k比特长度的随机数
# 11 -- 3
# 100, 111 -- 7
res10= random.getrandbits(6)
print(res10)
# 练习：生成随机的验证码，可以定义生成验证码长度，验证码包含，数字与字母（区分大小写）
def yanzm(length):
    az = [chr(i) for i in range(65,91)]
    AZ = [chr(j) for j in range(97,123)]
    num = [str(n) for n in range(0,10)]
    lt = az + AZ + num
    yan = ""
    for n in range(length):
        s = random.choices(lt)
        yan += s
    return  yan
print(yanzm(4))

def zy():
    checkcode = ""
    for i in range(4):
        k = random.randint(0,3)
        if k == i:
            b = chr(random.randint(65,90))
        else:
            b = random.randint(0,9)
        checkcode += str(b)
    print(checkcode)