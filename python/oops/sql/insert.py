import sqlite3

conn=sqlite3.connect('db/as_python')
sql = """ insert into stock values (1,'mango',80),
(2,'grapes',110),(3,'apple',150)"""

conn.execute(sql)
conn.commit()
conn.close()