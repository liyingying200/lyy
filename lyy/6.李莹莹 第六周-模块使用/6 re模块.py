"""
re模块：正则表达式，使用一定的规则（一些符号组合）去匹配一个目标字符串，得到我们想要的字符串
\n \r:换行符    \t:制表符
"""
# 1.\d:用来匹配字符串中一个数字 0-9
# 构建一个正则表达式
import re
pattern = re.compile(pattern ="\d",flags=0)
# 使用正则匹配
# match():根据正则表达式匹配字符串，从字符串开头位置进行匹配，第一个参数pattern：正则表达式，第二个参数string：目标字符串，第三个参数flags，默认是0；返回一个对象，可以通过方法group（）取值
res = re.match(pattern=pattern,string="123",flags=0)
print(res.group(0))
res1 = re.match(pattern="\d",string="2abc")
print(res1.group(0))
# 2.\w:用来匹配字符串中一个数字或字母（大小写）
res2 = re.match(pattern="\w",string="abc")
print(res2.group(0))
# 3.针对性匹配，要匹配特定的字母，数字，符号
res3 = re.match(pattern="a2",string="a279")
print(res3.group(0))
res31 = re.match(pattern="a\d",string="a024")
print(res31)
res32 = re.match(pattern="a\w",string="asf132")
print(res32)
# 4.点 . 可以匹配任意一个
res4 = re.match(pattern=".",string="*bc123")
print(res4.group(0))
res41 = re.match(pattern=".\d\w",string="-312")
print(res41.group(0))
# 5.+可以匹配+前字符任意多个
res5 = re.match(pattern="a+",string="aaaaaalj1233")
print(res5.group(0))
# .+可以匹配任意多个任意字符
res51 = re.match(pattern=".+",string="abc#*7%)!#")
print(res51.group(0))
# 6.* 可以匹配多个字符
res6 = re.match(pattern="a*",string="aaaaa")
print(res6.group(0))
res61 = re.match(pattern="\d*",string="12342abc")
print(res61.group(0))
# .*;.+可以匹配任意多个字符
res62 = re.match(pattern=".*",string="-=12874%6$*")
print(res62.group(0))
# 7.?可以匹配前边的字符0次或者1次，a？；可以匹配到也可以匹配不到
res7 = re.match(pattern="a?",string="bc123")
print(res7.group(0))
res71 = re.match(pattern=".?",string="199hueb32")
print(res71.group(0))
# 8.^ 上尖号，匹配以什么开头的字符串
res8 = re.match(pattern="^qwer",string="qwer1234")
print(res8.group(0))
res81 = re.match(pattern="^q.*2",string="qwer1234")
print(res81.group(0))
# 9.$,匹配以什么结尾的字符串
res9 = re.match(pattern=".*00$",string="17746238900")
print(res9.group(0))
# 10. | 连接两个正则表达式，或，符合两个正则其中一个
res10 = re.match(pattern="\d+|\w*",string="a123abc-=")
print(res10.group(0))