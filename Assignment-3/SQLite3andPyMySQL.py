# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.
import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO student (id, name, age) VALUES (1, 'Amit', 20)")

conn.commit()

cursor.execute("SELECT * FROM student")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()





#-----------------------------------------------Practical Example-------------------------------------#
#Write a Python program to create a database and a table using SQLite3. 
import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

conn.commit()

print("Database and table created successfully.")

conn.close()






# Write a Python program to insert data into an SQLite3 database and fetch it.
import sqlite3

conn = sqlite3.connect("student.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO student (id, name, age) VALUES (1, 'Amit', 20)")

conn.commit()

cursor.execute("SELECT * FROM student")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()