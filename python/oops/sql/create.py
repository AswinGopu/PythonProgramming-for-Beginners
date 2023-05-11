import sqlite3

conn = sqlite3.connect('db/as_python')
sql = """ create table stock(id int,
item text, price int)"""
conn.execute(sql)
conn.close()
