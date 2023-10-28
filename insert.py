import sqlite3

conn  = sqlite3.connect("example.db")
print("Opened database successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(1, 'EMOBILIS', '7', 'WESTLANDS', 250000.0)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(2, 'EMOBILIS', '7', 'WESTLANDS', 250000.0)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
             VALUES(3, 'EMOBILIS', '7', 'WESTLANDS', 250000.0)");

conn.commit()
print("The table connected successfully")
conn.close()
