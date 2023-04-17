"""
关键字参数：指定参数是什么，调用函数给参数传值
不定长参数：不确定参数有几个，可以传入多个参数,会打包成元组
不定长关键字参数：可以传入任意个关键字参数, 会将形参和实参打包成字典, 形参为键, 实参为值
"""

# 1.不定长参数，*取里面的数据
def funcl(*args):
    print(*args)
    print(args,type(args))
# 调用函数，传入任意个数据
funcl(1,2,3,4,5,6)
# 例：传入多个参数，将参数写入到集合中进行去重
print(*"1,2,3")
def add_set(*num):
    # print(set(num))
    set1 = set()
    for n in num:
        set1.add(n)
    print(set1)
add_set("西施","昭君","貂蝉")
# 2.不定长关键字参数
def func2(**kwargs):
    # print(**kwargs）
    print(kwargs,type(kwargs))
    print(kwargs["name"])
    for key,value in kwargs.items():
        print(key,value)
func2(name="秦始皇",xname="嬴政")
# 例：传入学生信息，拼接字符串输出
def stu_info(**students):
    name = students["name"]
    age = students["age"]
    sex = students["sex"]
    score = students["score"]
    string = ",".join([name,str(age),sex,str(score)])
    print(string)
stu_info(name="李四",age=19,sex="女",score=88)
# 练习1：使用不定长参数，传入数据，任意数据，需要数据判断，转化成子非常，然后输出后边，拼接--（数据类型）
def istype(*args):
    for data in args:
        tp = type(data)
        if tp == str:
            print(data + "--" + str(tp))
        elif tp == int:
            print(str(data) + "--" + str(tp))
        elif tp == float:
            print(str(data) + "--" + str(tp))
        elif tp == bool:
            print(str(data) + "--" + str(tp))
        else:
            # 传入的列表，元组有数字需要转化字符串拼接
            print(",".join(data) + "--" + str(tp))
istype(1,True,3.56,"hello",["2","a"],("hi",))

#  练习2：使用不定长的关键字参数，传入name,age,sex,将打包好的字典，字典的键转换，name-"姓名",age-"年龄".sex-"性别"
def sut_info(**kwargs):
    print(kwargs)
    kwargs["姓名"] = kwargs.pop("name")
    kwargs["年龄"] = kwargs.pop("age")
    kwargs["性别"] = kwargs.pop("sex")
    return  kwargs
res1 = sut_info(name="李莹莹",age=18,sex="女")
print(res1)
# 传入参数，起始数，终止数，计算该范围内的3和5的所有公倍数，放入列表返回
def func1(num1, num2):
    list1 = []
    for i in range(num1, num2+1):
        if i % 3 == 0 and i % 5 == 0:
            list1.append(i)
    return list1
res1 = func1(0, 100)
print(res1)
# 鸡兔同笼，头26个，脚44，当做参数传入函数时，计算并返回结果，鸡多少只，兔子多少只
def jttl(a,b):
    for x in range(1, a+1):
        y = a-x
        if 2*x + 4*y == b:
            print("鸡有" + str(x) + "只", "兔有" + str(y) + "只")
            return x, y
res2 = jttl(16, 44)
print(res2)

