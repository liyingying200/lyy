"""
双for循环嵌：外层循环没循环一次，内层循环循环所有次，内层循环体执行就是内外层循环次数的乘积
for i in 范围 ：    --循环9次
    for j in 范围:   --循环九次
         循环体

"""
# 1.双for
for x in range(3):
    for y in range(3):
        print("%d %d" % (x,y))
    print("这个属于外层循环的")
# 例：打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} x {j} = {i*j}", end="\t")
    print("")
"""
while-for 循环嵌套使用
while 判断条件：
     for i in 范围：
         循环体
"""
# 例：没有交作业，如果每次没有交作业，就说十遍我错了，三次机会结束
count = 0
while count < 3:
    print("猪八戒 没有交作业")
    for i in range(10):
        print("%d-我错了"%1)
    count += 1

# 回文数字，比如四位数数字5665，具有对称结构，找出1000-9999中所有的回文数字1111,2222，2112
for number in range(1000,10000):
    g = number % 10    # 取个位数
    q = number // 1000   # 取千位
    b = number // 100 % 10  # 取百位
    s = number %  100 // 10 # 取十位
    if g == q and b == s:
        print(number)
# 练习：斐波那契数列，第一项1，第二项1，第三项1+1 = 2
# 1 1 2 3 5 8...算出一百项
a =1
b = 1
for i in range(100):
    a = b
    b = a + b
    print(b)
# 练习：通过循环判断年龄处于什么阶段，如;幼儿0-6，儿童7-14，少年13-19，青年20-39，中年40-59，老年60以上

