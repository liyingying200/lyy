import random
caiq = ["石头","剪刀","布"]
stu = {"ming":0,"mao":0}
for n in range(10000):
    ming = random.choice(caiq)
    mao = random.choice(caiq)
    if ming == mao:
        print(ming,mao)
        print("平局，不得分")
    else:
        if ming=="石头"and mao=="剪刀":
            print("小明+1")
            stu["ming"] += 1
        elif ming == "剪刀" and mao =="布":
            print("小明+1")
            stu["ming"] += 1
        elif ming == "布" and mao =="石头":
            print("小明+1")
            stu["ming"] += 1
        else:
            print("小毛+1")
            stu["mao"] += 1
print(stu)
us_list = ["zhangsan","caimengdan","cc"]
password_list = [12345678,2345678,345678]
black_list = []
n = 1
while n <= 3:
    id = input("请输入你的id")
    if id in black_list:
        print("抱歉！您已被拉进黑名单")
        break
    while id not in us_list:
        print("请你注册后再登录")
        id = input("请输入你的id")
    print("账号输入正确")
    password = input("请输入用户对应的密码")
    s = us_list.index(id)
    pd = password_list[s]
    if password == pd:
        print("密码输入正确")
        print("登录成功")
        break
    else:
        print(f"密码输入不正确，还剩{3-n}次机会")
    n += 1
    if n == 3:
        black_list.append(id)
