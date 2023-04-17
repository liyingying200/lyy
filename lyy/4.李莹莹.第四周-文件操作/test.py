f = open("login.txt", encoding="utf-8")
users = f.read()
# 分割 split()
userlist = users.split("\n")
print(userlist)
# 分割账号-密码
userdict = {}
for user in userlist:
    res = user.split("-")
    userdict[res[0]] = res[1]
print(userdict)
un = input("账号：")
if un in userdict.keys():
    print("账号存在")
    # 验证密码
    pd = input("密码：")
    if pd == userdict[un]:
        print("密码正确")
    else:
        print("密码错误")
else:
    print("账号不存在")

"""
练习：打开一个文件year.txt，将1949-2022之间的闰年，写入文件中，每行写一个

"""
fy = open("year.txt","w",encoding="utf-8")
for y in range(1949,2023):
    if y % 4 == 0 and y % 100 !=0 or y % 400 == 0:
        fy.write(str(y) + "\n")
fy.close()
