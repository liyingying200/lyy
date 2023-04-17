"""
csv文件：逗号分隔符
"""
f = open(file="学员信息.csv",mode="a+",encoding="utf-8")
# 学员姓名：性别：班级：成绩
f.write("悟空,公，菩提1班，90")
f.write("八戒,公，天庭2班，70")
#  写入列表
list_stu = ["沙悟净","男","流沙河1班","60"]
# join():拼接字符串的方式
f.write(",".join(list_stu))
# 移动光标
f.seek(0)
text = f.read()
print(text)
f.close()
