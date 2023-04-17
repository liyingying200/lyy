# open():默认使用  模式是r，叫做只读模式
f = open("静夜思.txt",encoding="utf-8")
# 1.read():读取文本所有数据
all = f.read()
print(all)
# 2.readable()：结果是布尔值，True能读取数据
res = f.readable()
print(res)
# 3.seek:移动光标，参数offset:是相对指定位置的字节（注意：字母数字英文符号占一个字节，汉字占三个字节，utf-8字符集)偏移量；参数whence：表示所指定的位置，默认为0是文件开始位置，值为1是相对于文件的读写位置，值2相对于文件的结尾位置
s = f.seek(0)
print(s)
# 3.readline():读取一行数据，从光标所在的行读取数据，只读取一行数据，光标向后
line = f.readable()
print(line)
# 4.readlines():从光标开始读取数据，将每一行都拿到放入列表中，包括结尾的换行符
f.seek(0)
lines = f.readline()
print(lines)
# 5.tell():告诉你光标的位置
print(f.tell())

"""
# 练习: 在文件login.txt中添加一些账号密码 例如: liyingying-123465
# 1. 打开文件, 将所有的账号拿到
# 2. 键盘输入账号, 判断是否在文件中
"""
# liyingying-123456
# lisi123-123456
# root123-liyingying
# root000-www.baidu
fuser = open("login.txt", encoding="utf-8")
users = fuser.read()
# 分割split
userlist = users.split("\n")
print(userlist)
# 分割账号-密码
username = []
passwdord = []
for user in userlist:
    print(user)
    res = user.split("-")
    username.append(res[0])
    passwdord.append(res[1])
print(username)
print(passwdord)
# 判断账号是否存在
un = input("账号")
if un in username:
    print("账号存在")
    # 通过账号对应的索引，密码索引相同
    # 验证改账号的密码
    index = username.index(un)
    pd = input("密码：")
    if pd == passwdord[index]:
        print("密码正确")
    else:
        print("密码错误")
else:
    print("账号不存在")


