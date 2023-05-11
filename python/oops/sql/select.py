import sqlite3
conn= sqlite3.connect('db/as_python')
cur = conn.cursor()
sql = "select * from stock"
cur.execute(sql)

# res = cur.fetchall()
# print(res)
# print(res[0])

# res = cur.fetchone()
# print(res)
# print(res[0],res[1],res[2])
# res = cur.fetchone()
# print(res[0],res[1],res[2])
# res = cur.fetchone()
# print(res[0],res[1],res[2])

# print('-'*35)
# for(id,it,pr)in cur:
#     print("| %5d | %-10s | %10.2f |" % (id,it,pr))
#     print('-'*35)

# cur.close()
# conn.close()