import sqlite3
conn = sqlite3.connect('db/as_python')
sql = "update stock set price=120 where id = 1"
conn.execute()
conn.commit()
print("update succesfully")
conn.close()