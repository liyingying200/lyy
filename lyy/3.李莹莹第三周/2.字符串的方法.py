"""
字符串的方法：字符串名.方法()
"""
# 1.index():获取子字符串的首字符的索引,有多个重复取第一个
# 可以有起始位置，终止位置（取不到）
s1 = "to be or not to be"
index1 = s1.index("not")
print(index1)
index2 = s1.index("o")
print(index2)
index3 = s1.index("o",3,10)
print(index3)
# index4 = s1.index("a")
# ValueError: substring not found
# print(index4)

# 2.find():与index（）用法相同，找不到不会报错,会返回-1
s2 = "that is are question"
index4 = s2.find("are")
print(index4)
index5 = s2.find("a",3,9)
print(index5)
index6 = s2.find("1")
print(index6)
# 3.count():计算子字符串在原字符串中出现的个数
s3 = "年年岁岁花相似，年年岁岁人不同"
print(s3.count("年"))
print(s3.count("岁岁"))
# 4.spilt():分割字符串,返回一个列表，当不填参数，默认分割空格，\t,\n等。。。可以使用符号分割，字符都行，分割后，用于分割的字符没有了，每个的每部分都放入列表中，可以指定分割的最大数
s4 = "明眸、皓齿，冰肌、玉骨，冰*清，玉洁"
list1 =s4.split()
print(list1)
list2 = s4.split(",",2)
print(list2)
# 5.strip():默认去掉首尾的空格，可以去掉字符串首位的字符
s5 = "asd 123 ,./ "
print(s5.strip())
print(s5.strip("a"))
# 6.replace():替代
s6= "飞流直下三千尺，疑是银河落九天"
s1 = s6.replace("三","33")
print(s1)
s2 = s6.replace("九","56")
# 不能直接修改字符串的内容，例如列表修改元素

# 7.upper():将小写换成大写
s7 = "abc345"
print(s7.upper())
# 8.lower():将大写转换小写
s8= "abcDJI"
print(s8.lower())
# 9.join():拼接字符串，将序列拼接如字符串,这个字符串会将序列的每个元素进行分隔
list3 = ["计春华","徐锦江",'鳌拜']
s = "+".join(list3)
print(s)
