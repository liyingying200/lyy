"""
function
参数：在函数体中可以起作用，可以根据函数需要传入任何数据类型
形式参数（形参）：在定义函数时，提前写在括号内，用于函数体使用
实际参数（实参）：在调用函数时，传入一个参数，用于实际运算
def 函数名（参数）:
    函数体
    return 返回值
函数名（实参）

"""

# 1.传入一个数字参数，实现加法运算
def func1(x):
    print(x+100)
# 调用1
func1(10)
# 2.传入多个参数，实现加法
def func2(x,y,z):
    print(x + y + z)
#调用1，按照顺序写入，传参赋值就是参数的顺序
func2(1,3,4)
# 调用2：
func2(z=40,x=10,y=20)
# 传入不同类型数据
def stu_info(name, age, sex):
    print("姓名 = %s,age:%d,性别=%s"%(name ,age,sex))
stu_info(name="唐僧",age=40,sex="男")
# 4.传入列表类型
def xunhuan(list1):
    for num in list1:
        print(num)
list2 = [1,2,3,4,5]
xunhuan(list2)
xunhuan(list1=list2)
# 5.使用默认参数，再传入
def func5(a, b=2):
    c = a ** b
    print(c)
# 使用默认值，在传参数没有给定时，但是有，默认值，使用默认值
func5(a=100)
# 在传参给定了数据，使用传入实参，不使用默认值，使用参数
func5(a=10,b=3)

# 练习1：定义函数，传入参数，将参数连同值一起写入字典，设置参数，name，age，sex，cls，score
def stu(name,age,sex,cls,score):
    dict1 = dict(name=name,age=age,sex=sex,cls=cls,score=score)
    print(dict1)
stu(name="张三",age=18,sex="男",cls="智能",score=89)
# 练习2：传入一个四位数，判断是否为回文数，第一位与第四位相等，第二位与第三位相等
def hw(a):
    b = str(a)
    if len(b) == 4:
        if b[0] == b[-1] and b[1] == b[-2]:
            print("是回文数")
        else:
            print("不是回文数")
hw(2882)





