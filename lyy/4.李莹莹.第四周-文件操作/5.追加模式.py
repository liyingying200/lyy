"""
a:追加写模式，打开文本，文本不存在会创建，不会清空文本，会接着文本的末尾写入只会在末尾写入，与光标无关
"""
fa = open("水调歌头.txt","a",encoding="utf-8")
print(fa.readable())  # 不可读
print(fa.writable())  # 可写
#
fa.write("明月几时有，把酒问青天")
fa.seek(0)
fa.write("不知天上宫阙，今夕是何年")
fa.close()
"""a+:追加写读模式，打开文本，不会清空文本，会接着文本的末尾写入只会在末尾写入，与光标无关"""
faj = open("临江仙.txt","a+",encoding="utf-8")
print(faj.readable())  # 可读
print(faj.writable())  # 可写
faj.write("滚滚长江东逝水，浪花淘尽，是非成败转头空\n")
# 读取数据
faj.seek(0)
text = faj.read()
print(text)
faj.close()

"""
ab:二进制追加写
ab+:二进制追加写读
"""
fab = open("apple.png","ab+")
fab.seek(0)
print(fab.read())
fab.close()

"""
创建一个文件stus.txt，每行数据如下
学号123456789123-姓名：张三-性别：男-班级：智能2-成绩80
使用a+模式，键盘写入一些数据，大概10条
读取数据进行筛选，成绩低于60分还以上边格式写入补考文件
"""
f = open("stus.txt","a+",encoding="utf-8")
stu_num = input("学号：")
stu_name = input("姓名：")
stu_sex = input("性别：")
stu_cls = input("班级")
stu_mark = input("成绩：")
stuinfo = "学号：{}-姓名：{}性别：{}-班级：{}-成绩:{}\n".format(stu_num, stu_name, stu_sex, stu_cls, stu_mark)
print(stuinfo)
f.write(stuinfo)
# 读取数据
f.seek(0)
stu_list = f.readlines()
blist = []
for stu in stu_list:
    mark = stu.strip().split(":")[-1]
    if int(mark) < 60:
        blist.append(stu)
fb = open("补考.txt", "w", encoding="utf-8")
fb.writelines(blist)
fb.close()
f.close()

