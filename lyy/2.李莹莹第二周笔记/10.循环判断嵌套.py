#  例1. 20以内说奇数不说偶数
for i in range(1,21):
    if i == 13:
        continue
    if i % 2 == 0:
        print("过")
        continue
    print(i)
# 上边例子，当我们遇到13就跳过


