# 1.break :关键字，结束循环，当循环中遇到了break 循环就结束了
for i in range(10):
    if i == 6:
        # 当循环到i赋值为6，判断成立执行break，这个循环结束，后边代码不执行
        break
    print(i)
# 例：猜喜欢的人，猜三次
for n in range(3):
#     name = input("请输入张一山喜欢的人：")
    name = "杨紫"
    if name == "杨紫":
        print("我不同意")
        break
    else:
        print("接着猜")
# 2.continue ,关键字跳过，跳过当前某一次循环，后边循环继续
j = 1
while j < 20:
    if j == 13:
        print("跳过")
        j += 1
        continue
    print(j)
    j += 1
# 逢七必过
for i in range (1,100):
    if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
        print("跳过")
        continue
    print(i)
# "17"字符串中有没有7
for i in range(1, 100):
    if i % 7 == 0 or "7" in str(i):
        print("跳过")
        continue
    print(i)
# 练习，回文数字，比如四位数数字5665，具有对称结构，找出1000-9999中所有的回文数字1111,2222，2112



