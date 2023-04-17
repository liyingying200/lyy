"""
字典（dict）：使用大括号{}容器类型数据，由键值对（键与值之间使用冒号）构成的单位，他们用逗号隔开，形成了字典
  {"键1":值1，"键2"：值2...}
1.通过字典的键来获取值，不是通过索引，字典是无序的
2.字典的键是唯一的不重复的，不能修改
3.字典的值是可变的，值可以是任何数据类型，也可以是字典

"""

# 1.定义字典
# 空字典
dict0 = {}
print(dict0, type(dict0))
dit0 = dict()
print(dit0)
# 非空字典
dict1 = {"姓名":"张三","称号":"法外狂徒","创始人":"罗翔"}
print(dict1)
# 字典的键不重复，后边的键会将前边重复的覆盖掉
# dict2 = {"name":"大王","name":"大大王"}
# print(dict2)
# 列表能不能当字典的键,元组可以当键
# dict3 = {[1,2,3]: 123}
# TypeError: unhashable type: 'list'
# print(dict3)
dict3 = {(1,):1}
print(dict3)
# 通过函数创建非空字典
dict4 = dict([("1",1),("a",123)])
print(dict4)
dict5 = dict(a = 1,b = 2,c = 3,nams = "李四")
print(dict5)
dict6 = {}
# 赋值添加数据
dict6["hello"] = "jecker"
print(dict6)
# fromkeys():可以添加键，但没有值，值为None(没有，相当于myaql unll)
dict7 = {}.fromkeys(["name","age","sex"])
print(dict7)
# 2.给字典的赋值添加数据，修改数据
dict20 = {"姓名":"李白","诗歌":["静夜思","望庐山","蜀道难"]}
dict20["事迹"] = "杨贵妃研磨，高力士脱靴，唐明皇擦嘴"
dict20["位置"] = "打野"
print(dict20)
# 修改数据
dict20["称号"] = "诗仙"
dict20["称号"] = "青莲居士"
print(dict20)
# 3.删除数据，删除字典
del dict20["位置"]
print(dict20)
del dict20
# 4.pop():根据字典的键进行数据删除
dict40 = {"姓名":"哆啦A梦","伙伴":"大雄","年龄":"未知","性别":"公猫"}
dict40 .pop("伙伴")
print(dict40)
# 5.popitem()：删除一个键值对，从后边第一个删除的
dict40.popitem()
dict40.popitem()
print(dict40)

