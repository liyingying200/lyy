import re
from sql_tools import *


print(get_now_time())
print("""
    1. 查询所有班级的成绩
    2. 按照条件进行查询
""")
n = input(f"[{get_now_time()}] 输入选项: ")
# "^[12]&"          -- "1"
while not re.search(pattern="^[12]$", string=n):
    print("输入错误!")
    n = input(f"[{get_now_time()}] 输入选项: ")
if n == "1":
    res = select_sql(db="students.db", table="stu1210")
    for r in res:
        for i in r:
            print(i, end="\t")
        print()
elif n == "2":
    fit = input("输入条件(姓名=张三): ")
    if "姓名" in fit:
        res = re.search(pattern="[^\w]{1,2}", string=fit).group(0)
        f = ["name", res, fit.split(res)[-1]]
        res = select_sql(db="students.db", table="stu1210", f=f)
        for r in res:
            for i in r:
                print(i)
            print()
