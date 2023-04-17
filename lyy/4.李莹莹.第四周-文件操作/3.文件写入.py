"""
1.打开冰箱门2.把大象装进去3.关闭冰箱门
1.打开文件 2.写入文件/读取文件 3.关闭文件
"""
# 1.打开文件：以模式r打开，默认模式,文件不存在会报错
# 参数file:文件路径（绝对路径，相对路径），参数mode:打开模式，默认是r只读模式，参数encoding：指定编码字符集（utf-8，gbk不够312.。。）
f1 = open(file="静夜思.txt",mode="r",encoding="utf-8")
# 2.读取数据
print(f1.read())
# 3.关闭文件，打开文件会占用文件的操作权限，关闭文件会解除权限
f1.close()

# 1.打开文件：以模式w打开，文件不存在会创建；如果文件存在文件打开会清空文件内容
f2 = open(file="将进酒.txt",mode="w",encoding="utf-8")
# 2.写入数据，写入的是字符串
f2.write("君不见，黄河之水天上来，奔流到海不复回\n")
f2.write("天生我材必有用")
# writabl()：判断能不能写，返回布尔值
print(f2.writable())
print(f2.readable())
# wietlines():将序列内的数据写入文件中，是写入字符串
slist = ["\n李白","李","太白",123]
for index in range(len(slist)):
    if type(slist[index]) == str:
        pass
    else:
        slist[index] = str(slist[index])
f2.writelines(slist)
# 3.关闭
f2.close()

# 练习：打开一个文件，user.txt,账号-密码，账号密码键盘输入，输入前判断账号是否重复，不重复才能写入账号密码
fu = open("users.txt","w",encoding="utf-8")
user = input("账号：")
fr = open("users.txt","r",encoding="utf-8")
string = fr.read()
userpd = string.split("\n")
user_dict = {}
for upd in userpd:
    user = upd.split("-")[0]
    pd = upd.split("-")[1]
    user_dict[user] = pd
print(string)
if user in string:
    print("账号存在")
else:
    print("账号不存在")
    passwd = input("密码:")
    fu.write(user + "-" + passwd + "\n")

# 关闭
fu.close()
fr.close()
