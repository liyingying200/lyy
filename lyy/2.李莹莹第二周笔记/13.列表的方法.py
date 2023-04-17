"""方法，徐亚列表名.方法 使用"""
list1 = ["喜羊羊","懒羊羊","沸羊羊","美羊羊","暖羊羊","慢羊羊"]
# 1.index（）：获取元素的索引,当元素有多个取头一个元素的索引
x = list1.index("沸羊羊")
print(x)
# 2.count():计算元素在列表的个数
c = list1.count("沸羊羊")
print(c)
# 3.sort():对列表进行排序,根据元素的编码进行排序,默认列表升序排列（reverse=False）
list1.sort()
print(list1)
num_list = [1,23,45,56,78]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
# 4.append():可以向列表中添加元素,添加到末尾
list1.append("灰太狼")
print(list1)
list1.append("红太狼")
print(list1)
# 5.insert():根据索引插入元素，
list5 = ["成龙","小玉","老爹","特鲁","布莱克",]
list5.insert(0,"瓦龙")
print(list5)
list5.insert(3,"阿福")
print(list5)
# 6.extend():将两个列表按照顺序进行合并元素
list6 = ["亚梦","唯世","几斗"]
list6.extend(list5)
print(list6)
# 7.pop():删除元素,默认删除最后一个，可以根据索引删除对应的元素
list7 = ["海绵宝宝","派大星","章鱼哥","蟹老板","痞老板","珊迪"]
list7.pop()
print(list7)
list7.pop(3)
print(list7)
# 8.remove():移除元素，直接将对应元素移除,有多个重复元素，默认删除第一个
list7.remove("章鱼哥")
print(list7)
# 9.reverse():翻转列表
list7.reverse()
print(list7)
# 10.copy():克隆一个列表,新的与旧的内存地址不一样，不是同一个列表，元素一样
newlist = list7.copy()
print(newlist)
print(id(list7),id(newlist))
alist = list7
print(alist)
print(id(alist),id(list7))
# del 删除关键字
delis = [1,2,3,4]
del delis[-1]
print(delis)
del delis
print(delis)
# 11.clear():清空列表
delis.clear()
print(delis)