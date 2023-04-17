import sqlite3


def get_conn_cur(db: str):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return conn, cur
# select name, total_points from stu1210 where total_points >= 60;
# select name,class,stu_num from stu1210 where class = 人工智能2班;
def query_sql(table: str, query: list=None, f:list=None):
    conn, cur = get_conn_cur(db="students.db")
    s = lambda : ",".join(query) if query else "*"
    if f:
        t = lambda : str(f[-1]) if isinstance(f[-1], int) or isinstance(f[-1], float) else "'" + f[-1] + "'"
        f[-1] = t()
        w = " ".join(f)
        sql = f"""select {s()} from {table} where {w};"""
    else:
        sql = f"""select {s()} from {table};"""
    print(sql)
    cur.execute(sql)
    datas = cur.fetchall()
    cur.close()
    conn.close()
    return datas

if __name__ == '__main__':
    res = query_sql(table="stu1210",  f=["practice", ">=", 10])
    for r in res:
        print(r)
