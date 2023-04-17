"""
内置函数：print(),type(),id(),int(),len(),syr(),bool(),float(),sum(),max(),min()...
函数：实现某些功能，将实现功能的代码封装起来
自定义函数：函数相当于爆米花的炉子，参数相当于玉米，糖，油， 返回值（return）相当于爆米花
def: 定义函数的关键字
def 函数名（参数）：        --函数名，参数放入括号中
    函数体                 --函数体必须缩进在函数中
    :return 返回值         --返回值
函数名（）                 --调用函数
函数名命名规则：字母数字下划线，不能数字开头，不能与关键字冲突，不与内置函数冲突，见名知意
"""

# 1.定义函数，实现输入
def pt():
    print("迈克尔.杰克逊,I LOVE YOU")
# 调用函数
pt()
pt()
# 2.计算123456+7890
def  jisu():
    print(123456+7890)
jisu()
# 3.函数内定义变量
def chengfa():
    a = 100
    b = 789
    print(a*b)
chengfa()
# 4.函数循环列表
def forlist():
    list1 = [1,2,3,4]
    for l in list1:
        print(1)
forlist()
# 判断星期
def week():
    x = input("输入汉字星期：")
    if x == "星期一":
        print("today is monday")
    elif x == "星期二":
        print("today is tuesday")
    elif x == "星期三":
        print("today is wednesday")
    elif x == "星期四":
        print("today is thursday")
    elif x == "星期五":
        print("today is friday")
    else:
        print("today is weekend")
# week()
# 练习1：使用函数打印乘法表，10 * 10 乘法表
def cf():
    for i in range(1,11):
        for a in range(1,i+1):
            print(f"{i}x{a}={i*a}",end="\t")
        print("")
cf()
# 练习2：判断字符串，输入一个字母判断，输出该首字母对应的星期/月份英文
def week2():
    l = input("请输入首字母(小写)：")
    if l == "m":
        print("星期一")
    elif l == "t":
        print("星期二或星期四")
        y = input("输入星期第二个字母（小写）:")
        if y == "h":
            print("星期四")
        elif y == "u":
            print("星期二")
    elif l == "w":
        print("星期三")
    elif l == "f":
        print("星期五")
    elif l == "s":
        print("星期六或星期日")
        z = input("输出星期的第二个字母（小写）:")
        if z == "a":
            print("星期六")
        elif z == "u":
            print("星期日")
week2()
# 练习3：键盘输入一个三位数，判断是否为水仙数
n = []
def sx():
    k = int(input("请输入一个数字："))
    for x in range(100, 1000):
        bw = x // 100
        sw = x // 10 % 10
        gw = x % 10
        if x == bw ** 3 + sw ** 3 + gw ** 3:
            n.append(x)
    if k in n:
        print("正确")
    else:
        print("错误")
sx()
