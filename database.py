import sqlite3
'''Creates a database, this file only needs to be run once in order to setup the db file'''

#Connects to database
con = sqlite3.connect('medset.db')
#Enables foreign key support
con.execute("PRAGMA foreign_keys = ON")
#Creates a cursor
cur = con.cursor()

#Creates tables
cur.execute("""CREATE TABLE IF NOT EXISTS user (
        idUser INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birth INT
    )         
    """)

cur.execute("""CREATE TABLE IF NOT EXISTS medicine (
        idMedicine INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dose INTEGER,
        idUser INTEGER,
        FOREIGN KEY (idUser) REFERENCES user(idUser)
    )
    """)

cur.execute("""CREATE TABLE IF NOT EXISTS plan (
        idPlan INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        days INTEGER,
        time INTEGER,
        idMedicine INTEGER,
        FOREIGN KEY (idMedicine) REFERENCES medicine(idMedicine)    
    )""")

#Testing insert and database
#Table order
#User:
#0 id
#1 name
#2 birth

#medicine
#0 id
#1 name
#2 dose
#3 FK idUser

#plan
#0 id
#1 days
#2 time
#3 FK idMedicine

#If needs to search, use 'where' clause

"""things = [
    ('login', 2),
    ('register', 3),
    ('teste3', 4),
    ('teste4', 5)
]

cur.executemany("INSERT INTO user (name, birth) VALUES (?,?)", things)
cur.execute("SELECT * FROM user")
print(cur.fetchall())"""

#Commits command
con.commit()

#Closes connection
con.close()