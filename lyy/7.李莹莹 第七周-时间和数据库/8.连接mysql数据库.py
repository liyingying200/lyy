import pymysql
# 打开cmd命令窗口, 请输入下边的内容, 如果出现pip不是内部命令, python有毛病,请重新安装python
# pip install pymysql -i https://pypi.douban.com/simple
# pip install requests -i https://pypi.douban.com/simple
# 1. 创建连接和游标
# 本地地址: localhost/ 127.0.0.1
conn = pymysql.connect(host="localhost", user="root", passwd="123456", db="dming")
cur = conn.cursor()
# 2. 查询
cur.execute("select * from students;")
for r in cur.fetchall():
    print(r)
# 3. 关闭
cur.close()
conn.close()
