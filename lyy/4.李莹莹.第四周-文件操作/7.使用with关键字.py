""" with:上下文管理器，打开文件时不需要手动关闭"""
with open(file="水调歌头.txt",mode="r",encoding="utf-8") as f:
    # 代码块部分需要缩进，文件处于打开状态
    print(f.read())
"""
# with open(file="文件名",mode="模式",encoding="utf-8") as 变量:
    代码块
"""
# f.seek()
# 这里文件已经关闭

"""
练习：学号，姓名，性别，成绩  把这个当做表头写进cav文件，使用键盘输入添加数据，判断学号是否纯数字，判断学号是否为重复，性别是否为男女，成绩0-100，筛选出不及格的学生，写入新的csv文件，补考csv
"""
with open(file="学生成绩.csv",mode="a+",encoding="utf-8") as fs:
    # 判断第一行内容，判断是否有学号表头
    fs.seek(0)
    first_line = fs.readline()
    if "学号" not in first_line:
        fs.write("学号,姓名,性别,班级,成绩\n")  # 只写一次
    # 输入学生成绩信息；123456,张飞,男,蜀国,50
    stu_info = input("学生信息及成绩：")
    # 处理字符串 stu_info；split() 指定字符切割字符串，返回列表
    stu_list = stu_info.split(",")
    stu_num = stu_list[0]  # 取学号值
    stu_sex = stu_list[2]  # 取性别值
    stu_score = stu_list[-1]  # 取成绩
    # 取到文件的所有数据，长字符串
    fs.seek(0)
    string = fs.read()
    if stu_num.isdigit() and stu_num not in string:
        if stu_sex in ["男", "女"]:
            if stu_score.isdigit():
                if 0 <= int(stu_score) <= 100:
                    fs.write(stu_info + "\n")
                    print("学生信息已经录入！")
                else:
                    print("成绩大小不对！")
            else:
                print("成绩不是纯数字")
        else:
            print("输入的不是男女性别！")
    else:
        print("学号非纯数字或者已经存在")

    # 直接筛选学生的成绩
    fs.seek(0)
    students = fs.readlines()[1:]  # 列表，每行数据
    for stu in students:
        stulist = stu.split(",")
        score = stulist[-1].strip()
        if int(score) < 60:
            # 不及格成绩
            with open("补考.csv", "a+", encoding="utf-8") as fb:
                fb.seek(0)
                first_line = fb.readline()
                if "学号" not in first_line:
                    fb.write("学号,姓名,性别,班级,成绩\n")  # 只写一次
                fb.write(stu)
