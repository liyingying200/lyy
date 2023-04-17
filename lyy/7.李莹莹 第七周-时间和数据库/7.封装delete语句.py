import sqlite3

def get_conn_cur(db:str):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return conn,cur

def delete_sql(db:str,table:str,f:list):
    con,cur = get_conn_cur(db)
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


if __name__ == '__main__':
    con,cur = get_conn_cur(db="students.db")
#    cur.execute("""delete from stu1210 where name='孙铭辰';""")
#    con.commit()
    delete_sql(db="students.db",table="stu1210",f=["name","=","李莹莹"])
    con.commit()
