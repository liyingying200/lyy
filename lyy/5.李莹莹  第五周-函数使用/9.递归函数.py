"""
10! = 10*9*8*7*6*5*4*3*2*1
"""
def demo1(number):
    res = 1
    for n in range(1,number+1):
        res *= n
    return  res
res = demo1(100)
print(res)
# 递归函数：就是在函数的内部调用函数自己
def demo2(number):
    if number==0:
        return 1
    else:
        return demo2(number-1) * number
res2 = demo2(10)
print(res2)

