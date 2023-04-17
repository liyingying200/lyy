"""
1.使用函数，打印乘法表，乘法表格式用传入的参数决定，比如传入9，9就是99乘法表，结果将所有式子放入集合给返回值
2.使用函数，计算器实现，传入不定长关键字参数实现加减乘除计算器功能，比如传入12，22，"*"为12乘上22将结果返回
3.函数实现纯数字列表，元组的求最大最小值的功能，结果返回
4.函数实现数据分类，传入不定长关键字参数，通过字典取值判断，实现数据分类，将不同的数据类型写入csv文件，将写入文件的功能写成另一个函数，使用函数写入
注意，四道题都能实现的并可以课堂讲解每道题加2分
"""
# 1
def cfb(w):
    for m in range(w + 1):
        for n in range(1, m + 1):
            print(f"{m} x {n} = {m * n}", end="\t")
        print("")
cfb(9)
# 2
def jsj(**ab):
    a = ab["m"]
    b = ab["n"]
    w = a + b
    x = a - b
    q = a * b
    z = a / b
    return w, x, q, z
res1 = jsj(m = 11, n = 22)
print(res1)
# 3
def qz(x):
    list1 = []
    list2 = []
    for i in x:
        if i.isdigit():
            list1.append(i)
    a = max(list1)
    b = min(list1)
    c = [a, b]
    list2.extend(c)
    tuple1 = tuple(list2)
    return list1, tuple1
res2 = qz("183609mn你好")
print(res2)
# 4
def bdc(**dict1):
    a = []
    for valu in dict1.values():
        print(valu)
        if valu == int:
            print(f"整型:{valu}")
        if valu == str:
            print(f"字符串型{valu}")
        if valu == float:
            print(f"浮点型{valu}")
        a.append(valu)
    return a
res3 = bdc(int1=123, str1="你好中国", float1=3.1415)
print(res3)
def wj(x):
    f = open("数据类型.csv", "w+", encoding="utf-8")
    f.write(x)
    return f
res4 = wj(bdc)
print(res4)
