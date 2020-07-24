import sqlite3

db_file='sc.db'

conn=sqlite3.connect(db_file)

sql='select * from sc'

cur=conn.cursor()

cur.execute(sql)

print(cur.fetchall())

conn.close()