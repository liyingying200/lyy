"""
集合（set):使用{}，里面每个元素用逗号隔开，元素不重复，是无序的，元素不能修改，可以添加，删除

"""
# 1.集合定义，
# 空集合
set0 = {}      # <class 'dict'>
print(set0,type(set0))
set1 = set()
print(set1,type(set1))
# 非空集合
# 里面是数值，会自动排列
set2 = {1,2,3,4,5,6}
print(set2)
# 其他类型，随意排列
set3 = {"赵","钱","孙","李"}
print(set3)
# 放入重复数据，重复数据只保留一个
set4 = {"周","吴","郑","王","王","王"}
print(set4)
# 放入列表,TypeError: unhashable type: 'list'
# set5 = {"偶像",["朱一龙","李易峰","白宇","周星驰"]}
# print(set5)
# 放入元组,元组不能修改
set6 = {"偶像",("朱一龙","李易峰","白宇","周星驰")}
print(set6)
# 放入字典,TypeError: unhashable type: 'dict'
# set7 ={"偶像",{"男性":"周杰伦","女性":"迪丽热巴"}}
# print(set7)
# 放入集合 TypeError: unhashable type: 'set'
# set8 = {1,2,{1,2,3}}
# print(set8)
# 2.set()构建集合，类型转换
list1 = ["冯","陈","楚","魏"]
print(set(list1))
# 字符串转化成集合，字符串每个单位都是集合的一个元素
string = "ABCDEFGHIJKLMNOPQRST"
print(set(string))
print(list(string))
# 元组转化集合
tuple1 = (1,2,3,4,4,3)
print(set(tuple1))
# 字典转化集合，字典的键会放入集合，值没有
dict1 = {"姓名":"吕布","字":"奉先","特点":"专杀义父"}
print(set(dict1))
# 3.不可变集合
f1 = frozenset("你好，欢迎光临")
print(f1)
# 4.查询集合，只能遍历
set7 = {1,2,3,4,5,6,3,21,5,4}
for s in set7:
    print(s)
# 5.添加元素
# add():添加单个元素
set8 = {"关羽","赵云","张飞","张辽","黄忠"}
set8.add("魏延")
print(set8)
set8.add("姜维")
print(set8)
# update():添加多个元素
list2 = ["庞统","马超"]
set8.update(list2)
print(set8)
s = {"孙尚香","刘禅"}
set8.update(s)
print(set8)
# 6.删除元素
# remove():删除元素，如果删除元素不存在则会报错
set9 = {"袁绍","袁术","刘表","孙坚","公孙瓒"}
set9.remove("孙坚")
print(set9)
# set9.remove("刘备")
# print(set9)

# discard():删除元素,如果元素不存在不会报错
set9.discard("袁术")
print(set9)
set9.discard("曹操")
print(set9)
# pop():随机删除一个
set9.pop()
print(set9)
# clear():清空集合
set9.clear()
print(set9)
# 7.集合进行数学运算，并集，交集，差集
# 并集:两个集合所有的去重后元素
set10 = {1,2,3,4,5,6}
set11 = {2,4,6,8}
print("并集",set10 | set11)
# 交集：两个集合都有的元素
print("交集",set10 & set11)
# 差集:并集减去 被剪掉的集合元素
print("差集", set10 - set11)

