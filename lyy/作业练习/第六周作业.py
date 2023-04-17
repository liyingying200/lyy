# 1. 将考试的四道编程题写成代码运行无误后, 放一个py文件上交

# 1)请写出一段Python代码实现输出99乘法表，根据需求写出部分代码逻辑结构，正确输出运行结果
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i} x {j} = {i*j}", end="\t")
    print("")
# 2)请写出一段Python代码实现删除一个list里面的重复元素
list8 = ["海绵宝宝", "派大星", "章鱼哥", "蟹老板", "痞老板", "章鱼哥"]
list8.remove("章鱼哥")
print(list8)
# 3)苹果3元一个，鸭梨2元一个，桃子1元一个.现在想用200元买100个水果，请写出对应代码计算相应的组合，根据需求写出部分代码逻辑结构，正确输出运行结果
p = 1
y = 1
t = 1
for i in range(1, 101):
    if p * 3 * i + y * 2 * i + t * i == 200:
        print("zxc")

# 4)模拟用户登录验证的，实现用户名输入，密码输入及验证等，用户在3次内输入正确密码登陆成功，连续输错3次密码登陆失败，且该用户被记录在黑名单，黑名单中的用户被锁定不能再登陆，根据需求写出部分代码逻辑结构，完整实现功能
user = ["张三-男","李四-男","王五-女"]
hmd = []
passward = [123456,654321,555555]
user1 = []
sex = []
for u in user:
    list1 = u.split("-")
    user1.append(list1[0])
    sex.append(list1[1])
user2=""
h = 1
while h <=3:
    user2 = input("请输入账号:")
    if user1 in hmd:
        print("您的账号密码已输入错误三次,被加入黑名单,无法登录!")
    elif user2 in user1:
        c =user1.index(user2)
        print("账号输入正确!")
        passward1 =int(input("请输入密码:"))
        if passward1 == passward[c]:
            print("密码输入正确!")
            if sex[c] == "男":
                print(f"欢迎{user2}小哥哥登录")
                break
            else:
                print(f"欢迎{user2}小姐姐登录")
                break
        else:
            print(f"密码输入错误! 还有{3-h}次机会!")
            h +=1
            while h<=3:
                passward1 = int(input("请输入密码:"))
                if passward1 == passward[c]:
                    print("密码输入正确!")
                    if sex[c] == "男":
                        print(f"欢迎{user2}小哥哥登录")
                        break
                    else:
                        print(f"欢迎{user2}小姐姐登录")
                        break
                else:
                    h+=1
    else:
        print("账号不存在!")
if h >3:
    hmd.append(user2)
    print("账号已加入黑名单!")

# 2. 使用匿名函数判断出传入一个字符串学号是否属于本班学生
res1 = lambda id_class: "是本班学生" if 202101 <= id_class <= 202141 else "不是本班学生"
print(res1(202150))
# 3. 使用map函数, 传入一个列表, 将奇数与偶数分开
js = []
os = []
def num1(a):
    if a % 2 == 0:
        os.append(a)
    else:
        js.append(a)
    return f"奇数:{js}偶数{os}"
b = map(num1,[1, 2, 3, 4, 5, 6])
c = ""
for i in b:
    c = i
print(c)
# 4. 定义函数, 传入一个字典, 字典键为学生姓名, 值为学生成绩, 返回值是成绩的最大值与最小值
def dict1(a):
    b = a.values()
    b1 = list(b)
    b1.sort()
    return print(f"最大值{b1[-1]},最小值{b1[0]}")
dict1({"小王":99, "小明":88, "小白":87})
