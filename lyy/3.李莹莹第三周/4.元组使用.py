"""
列表（list）：使用[]，有序地，有索引，可重复数据，可放任何数据类型 ； 可进行增删改查
元组（tuple）使用（），有序地，有索引，可重复数据，可放任何数据类型 ；不能修改数据，不能添加数据，不能删除数据，只能查询
tuple  ("天机星","天罪星"，"天杀星","天罡星"
index      0        1        2        3     从0开始，递增
-index    -4        -3      -2        -1    从右往左依次递减
"""
# 1.定义元组
# 空元组
tuple0 = ()
print(tuple0, type(tuple0))
tuple00 = tuple()
print(tuple00)
# 定义一个元素的元组
# tuplel = (1)
# print(tuple1,type(tuple1))
tuple1 = (1,)
print(tuple1,type(tuple1))
# 放入多个数据的元组
tuple2 = ("小爱同学","jova","消毒消毒",123,2.35,True,[1,2,3],(1,2,3))
print(tuple2,len(tuple2))
# 最大索引，元组长度 -1
# 2.元组取值
print(tuple2[0])
print(tuple2[-1])
print(tuple2[len(tuple2) - 1])
# 3.进行切片操作
print(tuple2[1:])
print(tuple2[::2])
# 4.验证修改元组元素
# TypeError: 'tuple' object does not support item assignment
# tuple2[0] = "小a同学"

# 5.元组的加法，乘法
tuple3 = (1,2,3)
print(tuple3 + tuple3)
print(tuple3 * 20)
# 6.验证是否存在in，not in
if 1 in tuple3:
    print("在元组中")
# 7.元组的方法
# index():获取元组的元素索引，如果不存在元组会报错,有多个元素只返回第一个索引
print(tuple3.index(2))
# count():计算有多少个元素
print(tuple3.count(1))