import pandas as pd

lst = []
data = pd.read_excel('empdb.xlsx', sheet_name='performancerating')
records = data.to_records(index=False)
result = list(records)
for i in range(len(result)):
    print(result[i])

import sqlite3

conn = sqlite3.connect('empdb.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE performancerating(
    EmployeeID INTEGER,
    PerformanceRating INTEGER,
    PRIMARY KEY(EmployeeID)
    )
""")

for i in range(len(result)):

    cursor.execute(f"""
        INSERT INTO performancerating VALUES {result[i]}

    """)

cursor.execute("SELECT * FROM performancerating")

conn.commit()

conn.close()

print("Execution completed successfully")


