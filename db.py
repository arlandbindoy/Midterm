import sqlite3

conn=sqlite3.connect("database.db")
print("created database successfuly")
conn.execute("CREATE TABLE registration (Username TEXT,Email TEXT,Password PASSWORD,PRIMARY KEY(Username))")
print("Created a table Successfully")
conn.close