import sqlite3 

sqliteconnection = sqlite3.connect('first_example.db')
print("Database connected")

cursor = sqliteconnection.cursor()
print("Database initialized")

create_table_query = """
CREATE TABLE IF NOT EXISTS emp (id integer primary key autoincrement, name text,address text,age integer);
"""

cursor.execute(create_table_query)

insert_table_query = """
INSERT INTO emp(name, address, age) VALUES("Bishal","baneshowr","25")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name, address, age) VALUES("priyanka","siraha","26")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name, address, age) VALUES("Bibek","Golbazar","27")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name, address, age) VALUES("Ganesh","Golchakr","28")
"""

cursor.execute(insert_table_query)
sqliteconnection.commit()
sqliteconnection.close()

