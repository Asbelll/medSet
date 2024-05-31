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

#Commits command
con.commit()

#Closes connection
con.close()