"""
format():拼接字符串

"""
# 1.拼接字符串
name = "曹操"
say = "挟天子以令诸侯"
print("姓名：{0} 主要事迹：{1}".format(name,say))
print("姓名：{n} 主要事迹：{s}".format(s=say,n=name))
print(f"姓名：{name} {say}")
# 拼接浮点数
yi = 1.06
# .4f:保留浮点数后四位
print(f"补税：{yi:.4f}")
# 带符号 +
print(f"补税：{13.5:+.2f}")
# 不带小数点,四舍五入
print(f"{2.34:.0f}")
# 拼接整数,10d,占10个位置
age = 76
print(f"年龄{age:10d}")
# 位数不够前边补0
print(f"年龄{age:0>5d}")
print(f"年龄{age:*<5d}")
# 百分数格式化
gdp = 0.1516
print(f"国内生产总值：{gdp:.2%}")
# 调位置
print(f"{name: >10}")
print(f"{name: <10}")
print(f"{name:^10}")
# 判断字符串
string = "abcDEF"
# 1.isalpaha():判断为纯字母，是纯字母结果为true，否为false
if string.isalpha():
    print("纯字母")
# 2.isdigit():判断是否为纯数字，是结果为true，否为false
str2 = "123445"
if str2.isdigit():
    print("纯数字")
# 3.isalnum():
str3 = "abc123"
if str3.isalnum():
    print("是")
else:
    print("不是")
# 4.isupper():判断是否全部为大写
str4 = "WERASD"
if str4.isupper():
    print("都是大写")
# 5.islower():判断是否全部为小写
str5 = "abc"