# 1. 总结列表以及字符串的用法, 包括使用方法
"""
1.列表取值，可以通过索引取值；取值方法：列表名字[索引]
2.len()：计算列表的长度
3.列表切片，使用索引进行切片，用法：列表名[起始位置:终止位置:步长]，起始可以取到值，终止取不到值，左闭右开区间；在步长为正数，起始值必须小于终止值
4.列表的加法与乘法
   1)两个列表相加，或有序地将两个列表合成一个
   2)一个列表乘一个数，列表不会增加，里面元素个数是原来的n倍
5.检测元素是否为列表成员，使用in 或 not in
6.str()：将列表转换成字符串
7.sum()：计算元素的和，元素都是数值类型
8.max():计算最大值，返回列表中最大的元素
9.min():计算最小值，返回列表中最小的元素
10.sorted():对列表进行排序，默认升序排列
11.reversed():倒置列表，放入列表会返回一个生成器，需要用list()函数转换成列表
12.list():可以将其他数据转换成列表，字符串中每个元素都被转换成列表中单个元素
13.enumerate():将列表进行遍历，拿出 索引和对应的值
14.index():获取元素的索引，当元素有多个取头一个元素的索引
15.count():计算元素在列表的个数
16.sort():对列表进行排序，根据元素的编码进行排序，默认列表升序排列(reverse=False)，reverse=True 降序排列
17.append():可以向列表中添加元素，添加到末尾位置
18.insert():根据索引插入元素
19.extend():将两个列表按照顺序进行合并元素
20.pop():删除元素，默认删除最后一个，可以根据索引删除对应的元素
21.remove():移除元素，直接将对应元素移除，有多个重复元素，默认删除第一个
22.reverse():翻转列表
23.copy():克隆一个列表，新与旧的内存地址不一样，不是同一个列表，元素一样 del 删除关键字
24.clear():清空列表

字符串(str)：是一个有序的容器类数据，有索引，与列表相同
1.字符串定义：空列表([], list(), 相当于False)
string = ""    相当于False
s = str()      定义空字符串
2.字符串取值，同列表相似，也是使用索引，字符串名[索引]
3.字符串切片，和列表类似，左闭右开，右边取不到，起始位置不写默认为0索引，结束位置不写默认为字符串长度 步长：默认是1
4.字符串相加，拼接字符串
5.字符串乘数
6.判断字符串中是否有某个字符串
7.index():获取子字符串的首字符的索引，有多个重复取第一个  可以有起始位置，终止位置(取不到)；当找不到时会报错
8.find():与index()用法相同，找不到不会报错，会返回-1
9.count():计算子字符串中出现的个数
10.spilt():分割字符串，返回一个列表，当不填写参数，默认分割空格，\t，\n等...可以使用符号进行分割，字符都行，分割后，用于分割的字符没有了，每个的每部分都放入列表中，可以指定分割的最大数
11.strip():默认去掉首位的空格，可以去掉字符串首尾的字符
12.replace():替代   注意：字符串中的元素不能进行修改
13.upper():将小写转换成大写
14.lower():将大写转换小写
15.join():拼接字符串，将序列拼接如字符串,这个字符串会将序列的每个元素进行分隔
16.format():拼接字符串
  拼接字符串
  拼接浮点数
  4f:保留浮点数后四位
  带符号 +
  不带小数点，四舍五入
  拼接整数，10d，占十个位置
  位数不够前边补0
  百分数格式化
  调位置
  判断字符串
17.isalpha():判断是否为纯字母，是纯字母结果为True，否则为False
18.isdigit():判断是否为纯数字，是纯数字结果为True，否则为False
19.isalnum():判断字符串是否符号，没有符号为True，有符号为False
20.isupper():判断是否全部字母为大写
21.islower():判断是否全部字母为小写
"""
# 2. 完成学生信息记录
# 1) 定义一个列表, stu_list = [], 里面添加一个特定的数据, 每个数据是一个列表, 每个列表包括, 学生学号, 姓名, 性别, 班级, 按照顺序填写; 多维列表取值方法自己学一下
# 2) 实现功能1, 添加新的学生信息, 学号不能重复
# 3) 实现功能2, 根据学号可以删除学生的信息
stu_list = ["202115050201", "小明", "男", "2班"], ["202115050202", "小美", "2班"]
while True:
    print("""
    ------------------------
          学生信息记录表

          1.添加新的学生信息
          2.删除学生信息
          0.退出

    ------------------------
    """)
    a = ["0", "1", "2"]
    x = input("请输入您要使用的功能选项：")
    while x not in ["0", "1", "2"]:
        print("输入序号不正确")
        x = input("请输入您要使用的功能选项：")
    if x == "1":
        xue_hao = []
        for stu in stu_list:
            xue_hao.append(stu[0])
        print("添加新的学生信息")
        stu_id = input("请输入要添加的学生学号：")
        while not stu_id.isdigit():
            print("不是纯数字")
            stu_id = input("请重新输入要添加的学生学号：")
        else:
            while not len(stu_id) >= 12:
                print("你输入的学号长度不对(12)")
                stu_id = input("请重新输入要添加的学生学号：")
            else:
                print("输入学号长度正确")
            while stu_id in xue_hao:
                print("输入的学号已经存在")
                stu_id = input("请重新输入要添加的学生学号：")
            else:
                print("输入学号正确")
        stu_name = input("请输入要添加的学生姓名：")
        name = []
        for stu in stu_list:
            name.append(stu[1])
        while stu_name in name:
            print("你输入的姓名已经存在")
            stu_name = input("请重新输入要添加的学生姓名：")
        else:
            print("输入姓名正确")
        stu_xb = input("请输入学生性别：")
        xb = []
        for stu in stu_list:
            xb.append(stu[2])
        while stu_xb not in xb:
            print("输入性别错误")
            stu_xb = input("请重新输入要添加的学生性别：")
        else:
            print("输入性别正确")
        stu_class = input("请输入要添加的学生班级：")
        clas = []
        for stu in stu_list:
            clas.append(stu[3])
        while stu_class not in clas:
            print("输入班级不存在")
            stu_class = input("请重新输入要添加的学生班级：")
        else:
            print("输入班级正确")
            print("开始添加学生信息")
        a = input("你是否要添加学生信息(y/n)：")
        if a == "y":
            b = [stu_id, stu_name, stu_xb, stu_class]
            stu_list.append(b)
            print("添加信息成功")
            print(stu_list)
        else:
            print("添加信息失败")
    elif x == "2":
        xue_hao = []
        for stu in stu_list:
            xue_hao.append(stu[0])
        print("删除学生信息")
        stu_id = input("请输入要删除的学生学号：")
        while not stu_id.isdigit():
            print("不是纯数字")
            stu_id = input("请重新输入要删除的学生学号：")
        else:
            while len(stu_id) >= 12:
                print("输入学号长度不对(12)")
                stu_id = input("请重新输入要删除的学生学号：")
            else:
                print("输入学号长度正确")
                while stu_id not in xue_hao:
                    print("输入学号不存在")
                    stu_id = input("请重新输入要删除的学生学号：")
                else:
                    print("输入学号正确")
                a = input("是否要删除学生信息(y/n)：")
                if a == "y":
                    w = 0
                    for i in range(len(stu_list)):
                        if stu_id == stu_list[i][0]:
                            w = i
                        while stu_id in stu_list[w]:
                            stu_list.pop(w)
                            print("删除信息成功")
                else:
                    print("删除失败")
        print(stu_list)
    else:
        exit()




