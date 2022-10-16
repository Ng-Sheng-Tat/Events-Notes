import sqlite3
import pandas as pd

lst = []
data = pd.read_excel('empdb.xlsx', sheet_name='employee')
records = data.to_records(index=False)
result = list(records)

conn = sqlite3.connect('empdb.db')

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE employee(
    EmployeeID INTEGER,
    Age INTEGER,
    Department TEXT NOT NULL,
    DistanceFromHome INTEGER,
    EducationField TEXT,
    Gender TEXT,
    JobRole TEXT,
    MaritalStatus TEXT,
    MonthlyIncome INTEGER, 
    OverTime TEXT,
    PRIMARY KEY(EmployeeID)
    )
""")

for i in range(len(result)):

    cursor.execute(f"""
        INSERT INTO employee VALUES {result[i]}
    """)
    # print(result[i])

cursor.execute("SELECT * FROM employee")

res = cursor.fetchall()

for i in res:
    print(i)

# Commit command to the database
conn.commit()

# Close the connection explicitly
conn.close() 

print("Execution completed successfully")