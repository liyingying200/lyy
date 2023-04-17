# 格式化字符串
# 输出到文件中  ,open():打开一个文件，第一个参数是文件名字
# 第二参数是操作文件方式，w：write写入
file1 = open("data.txt","w")
# "".replace(":","\n")
print("通知：明天你们好像没有课",file=file1)

# 1.%s:占位符，可以拼接字符串型数据,拼接数据前判断是否为字符串，不是就转换数据类型，str（）
# 实际上可以拼接任何类型
name = "擎天柱"
print("汽车人首领：%s" %name )

number = 1223455  # int
print("我的电话号码是：%s"%number)
age = 18
gender = 80.5
print("%s的年龄是%s,成绩是%s"%(name,age,gender))
# %6.2s：里面的6表示拼接的字符串所占的占位数， .3表示取拼接的字符串前三个
# 如果占的位置不够，会自动变成与字符串本身长度一样的位置
word = "abcdefghigklmn"
print("%s"% word)
print("%.2s"% word)
print("%4.5s"% word)
print(len(word))

# %d:可以拼接整型数据,拼接数字类型数据可以，字符串不行，纯数字的字符串也会报错
print("张广师电话：%d"% number)
fl = 6.134
print("拼接小数：%d"% fl)
sl = "789"
# TypeError: %d format: a number is required, not str
# print("拼接字符串：%d"% sl)
# %02d:里面0表示在位数不够2的时候前边添加0,2表示占两个位置，当数字大于位置的时候，按数字的长度占位
year = 2002
month = 6
day = 1
money = 1.68
print("李昊生日：%d-%d-%d "% (year,month,day))
print("李昊生日：%d-%02d-%02d "% (year,month,day))
print("李昊有：%d" % money)

# 3.%f :可以拼接浮点型数据，默认保留小数点后6位，不够6位，补0
pi = 3.14
print("pi的值是：%f"% pi)
zs = 100
print("拼接整数看看:%f"% zs)
# %.3f:.3表示保留小数点后3位，四舍五入
pai = 3.1415626
print("π后保留2位：%.3f"% pai)

ip = 23.456
print("ip后保留2位：%.2f"% ip)

