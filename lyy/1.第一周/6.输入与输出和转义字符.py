# print():打印输出

# 1.输出函数
# 1）输出变量或常量
print("梅花香自苦寒来")
say = "宝剑锋从磨砺出"
print(say)
print("lyy",18,23)
# 2) 每次print都会换行，这是一个参数：end，默认为end="\n"
# \n:换行符，让字符串在这个地方另起一行
print("试试\n试试就逝世", end="!!!!!")
print("看看吧")
"""
\n 这种前边带\ 后边跟字母或数字，叫做转义字符
\ 会将后边的字母或数字一起转义，赋予其他意义
\t 制表符，相当于一个tab键
\\表示\，使用\取消\转义效果
"""
print("王小全\n年龄：78\n性别：男")
print("白起\t关云长\t蔡文姬\t程咬金")
print("banana\aplle")
print("\\")
print(len("\\"))
#  字符串前添加r也可以让字符串中的转义字符不再转义
print(r"姓名：黄忠\n年龄：78\n性别：男")
print("老话说得好：\'世上无难事，只怕有心人\'")
# \u4e00-\u9fa5:一，龥 所有汉字的编码范围在这个区间
print("\u4e00  \u9fa5")

# 2. input():输入函数，接收来自键盘输入的内容
# name = input("宝，你叫什么名字:")
# print(name)
# number = input("请输入您的余额")
# print(number, type(number))
# 有时需要数据类型转换
# number = int(number)
# print(number, type(number))

print("姓名：李莹莹\n年龄：18\n 成绩：良好\n性别：女")

