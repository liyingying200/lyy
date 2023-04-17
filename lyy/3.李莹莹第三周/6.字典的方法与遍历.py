# 1.循环字典
# key():可以拿到字典中所有的键
dict1 = {"姓名":"杜甫","代表作": ["登高","三吏","三别"],"称号":"少陵野老"}
print(dict1.keys())
# 转换列表
print(list(dict1.keys()))
for i in dict1.keys():
    print(i)
# values():可以拿到字典中所有的值
print(dict1.values())
print(list(dict1.values()))
for j in dict1.values():
    print(j)
# items():可以将键与值一起取出
for key,value in dict1.items():
    print(key,value)

# 2.字典方法
# 1） get():字典的取值方法,当取不到值的时候，使用第二个参数的定义值
dict2 = {"姓名":"苏轼","称号":"东坡居士","拿手菜":"东坡肉"}
name = dict2.get("姓名")
print(name)

# 2) setdefault():与get（）相似,当查询的键不存在字典中，会将键和使用的值添加进字典中
p = dict2.setdefault("拿手菜")
print(p)
l = dict2.setdefault("亲人",["苏洵","苏辙","苏小妹"])
print(l)
print(dict2)
# 3) clear():清空字典
dict2.clear()
print(dict2)
# 4) update():将一个字典合并到另一个字典中
dict3 = {"辛弃疾":"铁马冰河入梦来"}
dict1.update(dict3)
print(dict1)
# 5) python中的拷贝
dt = {"沈腾":"夏洛特烦恼","贾玲":"你好，李焕英","关晓彤":"木鸡啊",0:[1,2,3]}
# 赋值属于拷贝的一种，结果是数据相同，是同一个字典
dit = dt
print(dit)
print(id(dt),id(dit))
# copy():字典的方法,属于浅拷贝，字典虽然不是相同的id，但是内层嵌套的数据是相同的id，复制父对象，子对象不能复制
dt_copy = dt.copy()
print(dt_copy)
print("浅拷贝",id(dt[0]),id(dt_copy[0]))
# 使用模块，copy。deepcopy（）：深层拷贝,复制父对象，复制子对象
import  copy
dt_deepcp = copy.deepcopy(dt)
print(dt_deepcp)
print(id(dt[0]),id(dt_deepcp[0]))