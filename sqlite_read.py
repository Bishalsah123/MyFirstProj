import sqlite3 

sqliteconnection = sqlite3.connect('first_example.db')
print("Database connected")

cursor = sqliteconnection.cursor()
print("Database initialized")

sql_read_query = "SELECT * FROM emp;"
cursor.execute(sql_read_query)
print(cursor.fetchall())
sqliteconnection.close()