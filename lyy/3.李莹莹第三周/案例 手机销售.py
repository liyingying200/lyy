"""
手机销售
   1.多个品牌的手机
   2.功能
    1.添加功能
      1）查询是否有该手机，有则直接增加库存
      2）没有品牌则添加键值对（品牌及库存）
    2.查询手机品牌和库存
      1）单个查询，手机品牌及库存
      2）查询所有，将所有品牌及库存输出
    3.手机出售，选择一个品牌，选择购买数量，扣除库存，购买成功
      1）先查看品牌，选择购买的品牌
      2）输入购买数量，判断库存是否够用
      3）库存够输出可以购买，扣掉库存，购买成功
      4）库存不够，提示库存不够得进货，购买失败
    4.当手机没库存，删除这个手机品牌，删除库存
      1）手机库存为0，直接删除手机品牌
      2）可以手动修改库存数量


"""

phone_count = {"华为":800,"iphone":900,"小米":900,"vivo":800,"三星":600}
while True:
    print("""
    ---------------------
    欢迎使用手机销售商城
       1.添加手机信息
       2.查询手机信息
       3.手机销售功能
       4.删除库存信息
       0.退出
    ---------------------
    """)
    select_num = input("请输入您的选择序号：")
    while select_num not in ["0","1","2","3","4"]:
        print("输入序号有误")
        select_num = input("请重新输入您的选择序号：")
    if select_num == "1":
        print("添加手机信息")
        logo = input("请输入手机的品牌：")
        # 判断有没有该手机，phone_count.keys() 拿到所有键就是品牌
        if logo in phone_count.keys():
            print("品牌存在")
            print("请添加库存数量")
            num = input("新增手机数量（整数）：")
            while not num.isdigit():
                print("请输入纯数字")
                num = input("新增手机数量：")
            # 改变库存,就是修改字典的值
            phone_count[logo] += int(num)
            print(f"| 手机已入库，{logo}手机库存：{phone_count[logo]},新增:{num}")
        else:
            print("品牌不存在，将会添加到仓库")
            print("请输入库存数量")
            num = input("新增手机数量（整数）：")
            while not num.isdigit():
                print("请输入纯数字")
                num = input("新增手机数量：")
        # 改变库存,就是修改字典的值
        phone_count[logo] = int(num)
        print(f"| 手机已入库，{logo}手机库存：{phone_count[logo]},新增:{num}")

    elif select_num == "2":
        print("查询手机信息")
        if phone_count:
                print("""
                1.查询所有的手机信息
                2.按照品牌进行查询
                """)
                sn = input("请输入查询方式：")
                while sn != "1" and sn != "2":
                    print("输入序号错误")
                    sn = input("请输入查询的方式：")
                if sn == "1":
                    print("所有库存如下：")
                    for key,value in phone_count.items():
                        print(f"品牌：{key} 库存：{value}")
                else:
                    phone = input("请输入要查询的手机品牌：")
                    if phone not in phone_count.keys():
                        print("该手机不存在，请先添加信息")
                    else:
                        print(f"品牌：{phone} 库存：{phone_count[phone]}")
        else:
            print("没有任何库存信息可查询，请先添加")
        logo = input("请输入手机品牌：")
    elif select_num == "3":
        print("购买手机")
        print("所有库存如下：")
        for key, value in phone_count.items():
            print(f"品牌：{key} 库存：{value}")
        logo = input("请输入手机的品牌: ")
        while logo not in phone_count.keys():
            print("输入的手机品牌没有, 请重新输入")
            logo = input("请输入手机的品牌: ")
        print("请输入库存数量")
        num = input("购买手机数量(整数): ")
        while not num.isdigit():
            print("请输入纯数字")
            num = input("购买手机数量: ")
        # 判断购买的数量是否小于等于库存
        if int(num) <= phone_count[logo]:
            # 确认购买
            yn = input("请确认是否购买(y/n): ")
            if yn != "y" and yn != "n":
                print("输入错误, 返回")
            else:
                if yn == "y":
                    phone_count[logo] -= int(num)
                    print("购买成功")
                    print(f"| 手机已经出库, {logo} 手机库存: {phone_count[logo]}, 卖出: {num}")
                    if phone_count[logo] == 0:
                        del phone_count[logo]
                        print(f"{logo}品牌手机已经售卖完毕, 移除库存信息!")
                else:
                    print("取消购买, 返回")
        else:
            print("库存不足, 请重新购买")
    elif select_num == "4":
        print("删除库存信息")
        print("所有库存如下：")
        for key, value in phone_count.items():
            print(f"品牌：{key} 库存：{value}")
        print("""
                   1. 删除所有手机信息
                   2. 删除单个手机信息
                   3. 修改手机信息
               """)
        sn = input("请输入操作的序号: ")
        while sn != "1" and sn != "2" and sn != "3":
            print("输入序号错误")
            sn = input("请输入操作的序号: ")
        if sn == "1":
            print("确认是否清空库存信息")
            yn = input("请确认是否购买(y/n): ")
            if yn == "y":
                phone_count.clear()
                print("存库信息已经清空")
            else:
                print("正在返回")
        elif sn == "2":
            logo = input("请输入手机的品牌: ")
            while logo not in phone_count.keys():
                print("输入的手机品牌没有, 请重新输入")
                logo = input("请输入手机的品牌: ")
            print(f"确认是否删除{logo}牌品信息")
            yn = input("请确认是否删除(y/n): ")
            if yn == "y":
                phone_count.pop(logo)
                print(f"{logo}手机库存信息已经清空")
            else:
                print("正在返回")
        else:
            logo = input("请输入手机的品牌: ")
            while logo not in phone_count.keys():
                print("修改的手机品牌不存在, 请重新输入")
                logo = input("请输入手机的品牌: ")
            print("请输入库存数量")
            num = input("修改后手机数量(整数): ")
            while not num.isdigit():
                print("请输入纯数字")
                num = input("修改后手机数量: ")
            # 直接修改
            phone_count[logo] = int(num)
            print(f"修改后: {logo}手机 库存{num}")
            print("修改成功")
    else:
        exit()


