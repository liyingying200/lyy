"""1. 数字型
    整型(int): 就是整数, 包括正整数, 负整数, 0
     十进制: 0-9, -1, 0, +1
    八进制: 0-7, 满8进一, 0o100
    十六进制: 0-f, 满16进一, 0x100
    浮点型(float): 就是小数, 带有小数点的数
   2. 字符型
     字符串(str): 就是带引号的一句话, 单双引号没有区别
      "张飞"  "曹操"  "1422692191@q.com"  都是字符串
      多行注释也是字符串，是长字符串
   3. 布尔型（bool）：用于表达式结果，有两个值：
                         true：真，在数值上等于1，表示结果成立
                         false：假,在数值上等于0，

"""
"""
标识符命名规则
只能用字母，数字，下划线，切记不能用数字开头，数字开头会报错
规范：1.区分大小写，
        MySQL不区分大小写，Linux区分大小写
    2. 用小写字母给变量，对象，函数等命名，类的开头需要大写
    3.见名知意，看见名字就要知道内容数据大概情况，例如：name，age
    4.不要混淆，例如：字母o与数字0，字母l和数字1
    5.不要跟系统的关键字冲突，例：if，for，in，and
命名写法：多个单词命名时，可以用下划线，如：one_two_three
驼峰命名法：多个单词，第一个单词小写，后边单词首字母大写  getYouName,fullInLove
定义类时：FirstPerson

"""
# 定义一个学生的信息变量: 姓名, 性别, 年龄, 学号, 班级, 专业, 家庭地址   格式化输出信息
name = "小明"
gender = "男"
age = "18"
number = "2021150500209"
su_class = "2班"
major = "人工智能"
home = "河南省郑州市"
print("名字：%s, 性别:%s, 年龄：%s, 学号:%s, 班级：%s，专业：%s, 家庭住址：%s" % (name, gender, age, number, su_class,major, home))



# 4.将上述改为键盘输入每一项信息，然后打印格式化输出
name = input("姓名：")
print(name)
gender = input("性别：")
print(gender)
number = input("学号：")
print(number)
stu_class = input("班级：")
print(stu_class)
major = input("专业：")
print(major)
home = input("家庭住址：")
print(home)


