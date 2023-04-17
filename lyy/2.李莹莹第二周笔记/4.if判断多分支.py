"""
多分支结构是：程序从上往下运行，先进行第一个判断，如果条件成立，运行代码块1，运行完结束
if 表达式1:
    代码块1
elif 表达式2：
     代码块2
elif  表达式3：
     代码块3
。。。
else：
  代码块

"""

# 例1 ：0-59评为d，60-79评为c，80-89评为b，90-100评为a
score = input("输入成绩：") # 字符串类型
score = int(score)
if 0 <= score < 60:
    print("评分为D")
elif 60 <= score < 80:
    print("评分为C")
elif 80 <= score < 90:
    print("评分为B")
elif 90 <= score <= 100:
    print("评分为A")
else:
    print("输入成绩不正确")

# 例2：判断四季，春：3，4，5 夏：6,7,8 秋：9,10,11 冬：12,1,2
month = int(input("请输入月份："))
if month == 3 or month == 4 or month == 5:
    print("春:不知细叶谁裁出")
elif month in [6,7,8]:
    print("夏：小荷才露尖尖")
elif month in [9,10,11]:
    print("秋；月落乌啼霜满天")
elif month in [12,1,2]:
    print("冬;黑狗身上白，白狗身上肿")
else:
    print("地球上没有这个月份")

# 练习1：定义变量 variable 随便给数据，判断这个变量是什么数据类型
# 练习2：定义studay 周一到周五，判断是周几，然后输出专业课是那一节

var = 12.4
if type(var) == int:
    print("整数类型")
elif type(var) == "str":
    print("字符串类型")
elif type(var) == bool:
    print("布尔值类型")
elif type(var) == float:
    print("浮点型数据")
else:
    print("没有这个数据类型")

studay = "周一"
if studay == "周一":
    print("没课")
elif studay == "周二":
    print("第三四节")
elif studay == "周三":
    print("第七八节")
elif studay == "周四":
    print("第一二，五六节")
elif studay == "周五":
    print("第五六七八节")

