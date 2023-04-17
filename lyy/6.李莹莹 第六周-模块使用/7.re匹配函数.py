"""

"""
import re
# 1.match():从字符串开头进行匹配,匹配成功返回一个对象，匹配不成功返回none
res1 = re.match(pattern="abc\d\w+",string="labc123")
# print(res1.group(0))

# 2.search():从字符串任意位置进行匹配，如果匹配成功返回，如果有多个结果只返回一个
res2 = re.search(pattern="abc\d\w+",string="labc1234jia+abc234a")
print(res2.group(0))

# 3.findall():匹配字符串找到所有符合条件的子字符串，返回一个列表
# .*?:非贪婪匹配
res3 = re.findall(pattern="a.*?z",string="123azcsd89---a+z")
print(res3)

# 4.split():按照一定格式，对字符串进行分割,返回一个列表
res4 = re.split(pattern="\d",string="abdcjf9uufh_iw_897")
print(res4)

# 5.sub():一个新的字符替换一个旧的字符
res5 = re.sub(pattern="\d",repl="-",string="anbhs9sdn23jkbd8k9")
print(res5)
