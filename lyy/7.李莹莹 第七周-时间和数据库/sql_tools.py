import datetime
import sqlite3
import pymysql


# def get_conn_cur(db: str, dtype=None):
#     """
#     host: MySQL地址; port: 端口号; user: 账户, passwd/password: 密码; db: 数据库; charset: 字符集, 防止中文乱码
#     :param db:
#     :return:
#     """
#     conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="123456", db=db, charset="utf8")
#     if dtype==dict:
#         cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#     else:
#         cur = conn.cursor()
#     return conn, cur


def get_conn_cur(db: str):
    """
    连接数据库
    :param db:  数据库名字
    :return:
    """
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return conn, cur


def insert_sql(db: str, table: str, insert_info: dict):
    """
    查询语句
    :param table:   放入表名
    :param insert_info: 插入的数据, 字典形式, 字段为键, 插入数据为值
    :return:
    """
    conn, cur = get_conn_cur(db=db)
    if insert_info:
        klist = list(insert_info.keys())
        s = ",".join(klist)
        vlist = list(insert_info.values())
        h = lambda x: "'" + x + "'" if isinstance(x, str) else x
        vlist = [h(x) for x in vlist]
        f = lambda x: str(x) if isinstance(x, (int, float)) else x
        vlist = [f(v) for v in vlist]
        v = ",".join(vlist)
        sql = f"""insert into {table}({s}) values ({v});"""
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()


def select_sql(db: str, table: str, query: list = None, f: list = None):
    """
    查询语句
    :param table: 指定数据库中的表
    :param query: 查询的字段, 写参数, 默认是 * 查询所有
    :param f: 查询条件
    :return:
    """
    conn, cur = get_conn_cur(db=db)
    s = lambda: ",".join(query) if query else "*"
    if f:
        t = lambda: str(f[-1]) if isinstance(f[-1], int) or isinstance(f[-1], float) else "'" + f[-1] + "'"
        f[-1] = t()
        w = " ".join(f)
        sql = f"""select {s()} from {table} where {w};"""
    else:
        sql = f"""select {s()} from {table};"""
    # print(sql)
    cur.execute(sql)
    datas = cur.fetchall()
    cur.close()
    conn.close()
    return datas


def update_sql(db, table: str, up: dict, f: list = None):
    """
    更新语句
    :param table: 表名
    :param up: 更新的内容, {"major": "AI", "class": "AI2班"}
    :param f: 更新数据的筛选条件, ["class", "=", "人工智能2班"]
    :return:
    """
    con, cur = get_conn_cur(db=db)
    if up:
        ft = lambda x: str(x) if isinstance(x, (int, float)) else "'" + x + "'"
        t = [f"{k}={ft(v)}" for k, v in up.items()]
        c = ",".join(t)
    if f:
        t = lambda: str(f[-1]) if isinstance(f[-1], (int, float)) else "'" + f[-1] + "'"
        f[-1] = t()
        w = " ".join(f)
        sql = f"""update {table} set {c} where {w};"""
    else:
        sql = f"""update {table} set {c};"""
    print(sql)
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def delete_sql(db: str, table: str, f: list):
    """
    删除语句
    :param db:  数据库
    :param table: 要删除数据的表
    :param f: 数据筛选条件
    :return:
    """
    con, cur = get_conn_cur(db)
    if f:
        t = lambda: str(f[-1]) if isinstance(f[-1], (int, float)) else "'" + f[-1] + "'"
        f[-1] = t()
        w = " ".join(f)
        sql = f"""delete from {table} where {w};"""
    else:
        sql = """delete from {tbale};""".format(table)
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def get_now_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    con, cur = get_conn_cur(db="dming")
    cur.execute("select * from students;")
    print(cur.fetchall())   # 默认是元组形式