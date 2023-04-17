"""
1.map():将一个序列中每个元素，一一的传入函数中获取结果，第一个参数：函数，第二个参数：序列

"""
def funcl(num):
    return  num ** 2
# 调用
print(funcl(8))
# map():得到的结果是生成器,读一个数据少一个
res = map(funcl,[2,3,4,5,6,6])
print(list(res))
for r in res:
    print(r)
"""
2.reduce():将一个序列的元素，传入函数，先计算前两个，得到结果，再与第三个计算，第一个参数：函数，第二个参数：序列
"""
# 导入函数
from functools import reduce
def func2(x,y):
    return x + y
list2 = [a for a in range(1,11)]  # 列表推导式
print(reduce(func2,list2))
def func3(x,y):
    return x * y
t = (b for b in range(1,11)) # 生成器
for i in t:
    print(i)
# print(reduce(func3,t ))
"""
3.filter():将一个序列元素，传入函数，元素通过函数筛选结果为true的元素取出
"""
def even(num):
    return num % 2 == 0
res = (filter(even,[1,2,3,4,5]))
# print(list(res))
for r in res:
    print(r)
def year(y):
    return y%4 == 0 and y%100!=0 or y%400 == 0
# 使用列表推导式生成年份列表
yearlist = [year for year in range (1,2022)]
res2 = filter(year,yearlist)
print(list(res2))
# 使用匿名函数，结合高阶函数
odd = filter(lambda x: x % 2==1,[num for num in range(1,100)])
print(list(odd))
# 2.map
map_res = map(lambda n: n**10,[n for n in range(1,10)])
print(list(map_res))
# 3.reduce
rea = reduce(lambda x,y: x -y ,(n for n in range(1,100)))
print(rea)
"""
练习1：使用高阶函数map（），筛选出3,5的公倍数，筛选函数写普通函数或匿名函数
练习2：使用高阶函数filter()，筛选出100-1000的水仙花数
3.使用高阶函数，将两个列表，一个是名字，一个是成绩，按照顺序一一结合放入字典中
"""
# 1
gbs = filter(lambda g:g %3==0 and g %5==0,[g for g in range(1,100)])
print(list(gbs))
# 2
def l(wq):
    ge = wq % 10
    shi = wq // 10 % 10
    bai = wq // 100
    return ge ** 3 + shi ** 3 + bai ** 3 == wq
sxh = filter(l,[c for c in range(100,1000) ])
print(list(sxh))


# zip():将序列两两结合进行计算
res = zip([1,2,3,4],["a","b","c"])
print(dict(res))
# for r in res:
#    print(r)b e
