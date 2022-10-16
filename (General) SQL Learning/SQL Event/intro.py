import sqlite3

conn = sqlite3.connect('test.db')

cursor = conn.cursor()



cursor.execute("SELECT * FROM testtable")

res = cursor.fetchall()

for i in res:
    print(i)

conn.commit()

conn.close()