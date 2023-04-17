import re

# 1. {n}: 匹配{}前边字符出现的次数, 匹配n次
res1 = re.search(pattern="@{3}", string="1@23@@@1234@@456")
print(res1.group(0))
# {n,}: 至少匹配n次
res2 = re.findall(pattern="j{1,}", string="jsdfghjjj123jjjjjjj")
print(res2)
# {n,m}: 最少匹配n次, 最多匹配m次
res3 = re.findall(pattern="c{1,3}", string="c, abcc, cccccc")
print(res3)
# 2. []: 表示匹配的范围, \d匹配一个数字, [0-9]表示匹配的数字0到9
# [0-9]: 匹配0到9中一个数字
res4 = re.findall("[0-9]", string="123abc890jl8lkj7h6")
print(res4)
res5 = re.findall("[0-9]{1,30}", string="123abc890jl8lkj7h6")
print(res5)
# [a-zA-Z]: 匹配字母, 无论大小写字母
res6 = re.findall("[a-zA-Z]{1,3}", string="123abc890jl8lkj7h6ABC")
print(res6)
# [0-9a-zA-Z]: 匹配数字, 小写字母, 大写字母
res7 = re.findall("[a-zA-Z0-9]{1,3}", string="123abc890jl8lkj7h6ABC")
print(res7)
# [^0-9]: 出去0-9之外的都可以
res8 = re.findall("[^a-zA-Z0-9]{1,3}", string="123abc89%%0jl**8lkj7h6ABC")
print(res8)
# 3. (): 表示括号中是可以单独取出来的数据, 使用 | 将不同的正则或连接
res9 = re.findall("张(.)强", string="张强, 张小强, 张大强, 苏大强, 刘华强, 许文强")
print(res9)
res10 = re.search(pattern="姓名叫(.{1,10})年龄([0-9]{1,3})", string="我的姓名叫罗翔年龄48, 外号张三")
print(res10.group(0))
# group(0): 匹配真个正则匹配内容, group(1): 我们定义第一个()匹配到的内容 group(2)是第二个()内容
print(res10.group(1))
print(res10.group(2))
# groups(): 将所有()内匹配到的内容放入元组返回
print(res10.groups())
# 练习: 使用正则, 匹配qq号; qq: 6-10, 不能以0开头
res = re.search(pattern="^[1-9][0-9]{5,9}$", string="123456789")
if res:
    print(res.group(0))
else:
    print("字符串不是qq")
