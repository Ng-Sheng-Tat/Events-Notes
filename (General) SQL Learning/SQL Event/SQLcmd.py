import sqlite3

conn = sqlite3.connect('empdb.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE defaulttable(
        def_id INTEGER,
        column1 TEXT,
        column2 TEXT DEFAULT 'DEFAULT INPUT',
		PRIMARY KEY(def_id)
    )
""")

cursor.execute("""
    INSERT INTO defaulttable(def_id, column2)
    VALUES(1, 'string1')
""")

cursor.execute("""
    INSERT INTO defaulttable(def_id)
    VALUES(2)
""")

cursor.execute("SELECT * FROM defaulttable")
# if not specify it will be null or none


res = cursor.fetchall()

for i in res:
    print(i)

# Commit command to the database
conn.commit()

# Close the connection explicitly
conn.close()

print("Execution completed successfully")