import sqlite3
"""
sqlite,mysql 都是属于关系型数据库，使用sql语法是一样的
"""
#  1.创建一个数据库的连接
# connect(数据库名）：会链接数据库，如果数据库不存在会创建一个数据库文件，返回连接对象
# connection：可以用来创建游标，提交事务，回滚事务，关闭连接
connection = sqlite3.connect("student.db")
# 2.使用连接对象创建游标（用来执行sql语句，读取结果数据）
cursor = connection.cursor()
# 执行sql语句创建一个表
create_sql = """
    create table if not exists stu(
        id int primary key,
        name varchar(20) not null,
       phone char(11) unique 
    );
"""
# 3.使用游标执行sql语句
cursor.execute(create_sql)
# 4.插入数据
insert_sql = """insert into stu(id,name,phone) value (20110422,"张百忍"，198888788)"""
# cursor.execute(insert_sql)
# 查询数据
select_sql = """select * from stu;"""
cursor.execute(select_sql)
# 通过游标取出数据
res = cursor.fetchone()    # fetchone（）：从查询结果中读取一条数据，以元组形式返回
print(res)
res2 = cursor.fetchall()   #
print(res2)
res3 = cursor.fetchmany(2) # fetchmany(size):从结果中读取指定size个数的数据

# 操作sqlite3模块是添加数据，修改，删除数据当做一个事务处理，需要提交才能生效
# 5.提交数据，commit（）提交事务
connection.commit()
# 6.整个操作结束，关闭游标
cursor.close()
# 7.关闭连接
connection.close()
# pip install  pymysql -i https://pypi.douban.com/simple