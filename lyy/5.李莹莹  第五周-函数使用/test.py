"""
使用csv文件操作和函数实现登录功能
1.创建一个csv文件，第一列是账号，username，第二列密码，password；提前一两个账号，密码用于验证
2.将查询账号的功能进行函数封装，调用函数得到所有的账号放入一个列表中，用于判断
3.查询密码函数，传入一个参数是账号，打开文件找到这个账号对应的密码作为返回值
"""
def check_user(file_name="login.csv"):
    with open(file_name, "r", encoding="utf-8") as f:
        user_list = f.readlines()[1:]
        user_dict = {user.strip().split(",")[0]: user.strip().split(",")[1] for user in user_list}
        return user_dict
    # 验证账号密码


count = 1
black_list = []
while count <= 3:
    user = input("账号: ")
    if user in black_list:
        print("你已经被拉黑, 请联系客服人员: 15136282191")
        break
    while user not in check_user().keys():
        print("输入账号不存在, 请重新输入")
        user = input("账号: ")
    passwd = input("密码: ")
    if passwd == check_user()[user]:
        print("登陆成功")
        break
    else:
        print("密码错误")
        if count == 3:
            black_list.append(user)
        else:
            count += 1
