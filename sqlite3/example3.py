import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

# To fetch all tuple from table
cursor.execute("SELECT * FROM employee") 
print("fetch all:")
result = cursor.fetchall() 
for r in result:
    print(r)

# To fetch only first tuple from table
cursor.execute("SELECT * FROM employee") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)