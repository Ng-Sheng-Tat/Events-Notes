import sqlite3
import os
import pandas as pd

conn = sqlite3.connect('empdb.db')

cursor = conn.cursor()


# cursor.execute("""
#     CREATE TABLE dummytable(
#         IDnumber TEXT,
#         Date DATE
#     )
# """)

# Repeat for multiple times
cursor.execute("""
    INSERT INTO dummytable VALUES(3, "2021-1-5")
""")

cursor.execute("""
    INSERT INTO dummytable VALUES(2, "2021-1-2")
""")

cursor.execute("""
    INSERT INTO dummytable VALUES(1, "2021-1-3")
""")
    
cursor.execute("SELECT * FROM dummytable WHERE date = '2021-1-5'")

res = cursor.fetchall()

for i in res:
    print(i)

# Commit command to the database
conn.commit()

# Close the connection explicitly
conn.close()


print("Execution completed successfully")
