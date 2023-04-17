"""
匿名函数（虚函数）：不需要命名，一般只使用一次，简化定义函数的代码，使用lambda关键字定义，可以使用参数，返回值，可以集合判断，不结合循环
def 函数名（）

"""
# 1.输出函数
def say():
    print("这个是传统函数")
# ():起到的作用是执行这个函数
say()
print(say)
# 匿名实现
res = lambda : print("这是匿名函数")
res()
# 2.添加参数
res2 = lambda x : print(x ** 10)
res2(10)
res22 = lambda x, y: print(x * y)
res22(4,5)
# 3.传入序列
res3 = lambda dict1 : print(dict1["name"])
res3({"name":"吴老狗"})
# 4.结合判断，添加返回值
res4 = lambda name: "我爱中国" if name == "周恩来" else name
n = res4("周恩来")
print(n)
res44 = lambda score: "及格" if score >= 60 else "不及格"
print(res44(80))
# 练习1：判断一个数字是否为负值，是负值返回true，不是返回false
res5 = lambda shu:"True" if shu < 0 else "False"
print(res5(3))
# 练习2：判断列表的长度，如果是空列表，返回“空”，不是空列表，返回列表第一个值
res6 = lambda list2:"空" if list2 == [] else "非空"
print(res6([2]))
# 练习3：定义一个函数，传入不定长参数，经过筛选将奇数放入一个列表中，这个列表定义为全局变量，使用匿名函数获取这个列表的元素个数
def x(w):
    global a
    a = []
    for i in w:
        if i % 2 != 0:
            print("奇数")
            a.append(i)
        else:
            print("错误")
    print(a)
x([m for m in range(1,100)])
res7 = lambda m: print(len(a))
res7(a)