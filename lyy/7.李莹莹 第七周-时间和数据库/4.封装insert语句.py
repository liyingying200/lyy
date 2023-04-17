import sqlite3
# insert into stu(id,name,phone) value (20110422,"孔丘"，198888788)
# {"id": 20020410, "name":  "孔丘", "phone": 1588888882}
# insert into {}({}) values ({})
def get_conn_cur(db:str):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    return conn,cur

def insert_sql(table:str,insert_info:dict):
    conn,cur = get_conn_cur(db="student.db")
    if insert_info:
        klist = list(insert_info.keys())
        s = ",".join(klist)
        vlist = list(insert_info.values())
        h = lambda x :"'" + x + "'" if isinstance(x,str) else x
        vlist = [h(x) for x in vlist]
        f = lambda x :str(x) if isinstance(x,int) else x
        vlist = [f(v) for v in vlist]
        v = ",".join(vlist)
        sql = f"""insert into {table}({s}) value ({v});"""
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    # conn,cur = get_conn_cur(db="mydb.db")
    # insert_sql(table="stu", insert_info={"id": 20020420, "name":  "李耳", "phone": 1588888880})
    insert_sql(table="stu", insert_info={"id": 20020422, "name": "金蝉子", "phone": 1598888880})
