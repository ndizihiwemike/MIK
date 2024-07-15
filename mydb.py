#python database, sqlites3, postgress
import sqlite3

conn = sqlite3.connect('test.db')
print("opened database successfully")

# AUTOINCEREMENT
try:
    conn.execute("""
CREATE TABLE COMPANY(
      ID INT PRIMARY KEY NOT NULL,
      NAME TEXT NOT NULL,
      AGE INT NOT NULL,
      ADDRESS CHAR(50),
      SALARY REAL):
        """)
    print("Table created successfully")
except:
    pass

def insertData():
    conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES \
        (1, 'Paul', 32, 'califonia', 20000.00)")

    conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (2, 'Allen', 25, 'texas', 20000.00)")
    
    conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (3, 'Mike', 21, 'England', 20000.00)")
    
    conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)\
        VALUES (4, 'Babra', 28, 'mexico', 20000.00)")
    
    conn.commit()
    print("Records created successfully")

#insertData()

def all_entries():
    cursor = conn.execute("SELECT * from COMPANY")
    for row in cursor:
        print('ID =', row[0])
        print("NAME =", row[1])
        print("ADDRESS =", row[2])
        print("salary =", row[3],"\n")

        print("operation done successfully")    

#all_entries()

def update_users():
    conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
    conn.commit()
    print("Total number of rows update :", conn.total_changes)

#all_entries()

def delete_users():
    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)