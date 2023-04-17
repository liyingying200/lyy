"""
列表推导式，字典推导式，生成器

"""
# 1.列表推导式
list1 = list()
for i in range (1,101):
    list1.append(i)
print(list1)
# 推导式
list2 = [i for i in range(1,101)]
print(list2)
# 使用list转换
list3 = list(range(1,101))
print(list3)
# 生成字符串列表
list4 = [s for s in "ABCDE"]
print(list4)
# 2.字典推导式
dict1 = {index:value for index ,value in enumerate(list1[:10])}
print(dict1)
dict2 = {k:v for k,v in enumerate("asdfghj")}
print(dict2)
# 3.生成器;next():可以取出一个生成器的值；一个一个取出生成器中的值
# <generator object <genexpr> at 0x00000242BAB79390>
g = (i for i in range(10))
print(g)
print("取出一个值",next(g))
print("取出一个值",next(g))
# print(list(g))
for i in g:
    print(i)