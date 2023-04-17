"""
登陆注册系统.
        1.登陆
            键盘输入: 账号,密码 都是字符串.
            username_list = []      账号的列表
            password_list = []      密码的列表
            注意: 账号和密码在列表中存放的索引要一一对应
            1.从键盘上输入一个账号, 判断列表中有没有这个账号.
            2.如果有说明账号存在, 下一步去验证密码
            3.通过账号的索引跟密码在列表中的索引一致. 通过索引找密码
            4.验证密码通过则登陆成功.
        2.注册
            1.输入账号, 验证是否存在, 存在则重新输入, 不存在则注册
            2.输入密码保存在密码列表中
        3.修改密码
            1.先登录, 然后获取账号的索引
            2.根据账号的索引获取到密码进行修改
        4.删除账号
            1.先输入账号, 然后获取账号的索引, 删除账号
            2.根据账号的索引获取到密码进行删除
"""

username_list = ["root001"]
password_list = ["123456"]
while True:
   print("""
   --------------------
      欢迎使用河南艺术职业学院官网
          1.登录账号
          2.注册账号
          3.修改密码
          4.删除账号
          0.退出
   -----------------------
   """)
   # 选择功能
   select_num = input("请选择您要使用的功能选项")
   # 判断是否输入的是正确序号
   while select_num not in ["0","1","2","3","4"]:
      print("输入序号不正确")
      select_num = input("请选择您要使用的功能选项：")
   if select_num == "1":
      print("登录账号")
      username = input("请输入您的账号（6-20）：")
      while not 6 <= len(username) <= 20:
         print("输入账号长度不对，请重新输入：")
         username = input("请输入您的账号（6-20）：")
      if username in username_list:
         print("请输入密码：")
         password = input("密码（6-20）：")
         while not 6 <= len(password) <=20:
            print("输入密码长度不对，请重新输入：")
            password = input("请输入您的密码：")
         # 验证输入密码是否正确
         index = username_list.index(username)
         passwd = password_list[index]
         if password == passwd:
            print("登陆成功，请使用")
         else:
            print("输入密码错误")
      else:
         print("账号不存在，请注册")

   elif select_num == "2":
      print("账号注册")
      username = input("请输入您的新账号（6-20）：")
      while not 6 <= len(username) <= 20:
         print("输入账号长度不对，请重新输入")
         username = input("请输入您的账号(6-20):")
      while username in username_list:
         print("账号已被注册，请重新输入：")
         username = input("请输入您的账号（6-20）：")
      # 将输入的账号添加列表中
      username_list.append(username)
      print("请输入密码：")
      password = input("密码（6-20）：")
      while not  6 <= len(password) <=20:
         print("输入密码长度不对，请重新输入：")
         password = input("输入您的密码（6-20）：")
      # 把密码放入列表中
      index = username_list.index(username)
      password_list.insert(index,password)
      print("账号注册成功")
   elif select_num == "3":
      print("修改密码")
      username = input("请输入您的账号（6-20）：")
      while not 6 <= len(username) <= 20:
         print("输入账号长度不对，请重新输入：")
         username = input("请输入您的账号（6-20）：")
      if username in username_list:
         print("请输入密码：")
         password = input("密码（6-20）：")
         while not 6 <= len(password) <= 20:
            print("输入密码长度不对，请重新输入：")
            password = input("请输入您的密码（6-20）：")
         # 验证输入密码是否正确
         index = username_list.index(username)
         passwd = password_list[index]
         if password == passwd:
            print("登陆成功，请输入新密码：")
            pd = input("新密码（6-20）：")
            while not 6 <= len(pd) <= 20:
               print("输入新密码长度不对，请重新输入：")
               pd = input("请输入您的新密码（6-20）：")
            # 验证新旧密码是否一致
            while pd == passwd:
               print("输入新密码与旧密码一致，请重新输入：")
               pd = input("请输入您的新密码（6-20）：")
            # 修改密码为新密码
            password_list[index] = pd
            print("新密码修改完成")
         else:
            print("输入密码错误")
      else:
         print("账号不存在，请注册后在登录")
   elif select_num == "4":
      print("删除账号")
      username = input("请输入您的账号（6-20）：")
      while not 6 <= len(username) <= 20:
         print("输入账号长度不对，请重新输入：")
         username = input("请输入您的账号（6-20）：")
      if username in username_list:
         print("请输入密码：")
         password = input("密码（6-20）：")
         while not 6 <= len(password) <= 20:
            print("输入密码长度不对，请重新输入：")
            password = input("请输入您的密码（6-20）：")
         # 验证输入密码是否正确
         index = username_list.index(username)
         passwd = password_list[index]
         if password == passwd:
            print("登陆成功，请确认是否删除")
            yn = input("请确认是否删除当前账号（y/n:")
            while yn not in ["y","n"]:
               print("请输入y/n")
               yn = input("请确认是否删除当前的账号(y/n):")
            if yn == "y":
               del username_list[index]
               print("账号已注销")
         else:
             print("输入密码错误")
      else:
         print("账号不存在，请注册后登陆")
   else:
      exit()  # 结束程序





