import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

# only run one time
c.execute(''' CREATE TABLE Salesperson (
            ID integer,
            Name text,
            Age integer,
            Salary integer)
        ''')
#only run one time

c.execute('''INSERT INTO Salesperson VALUES
            (1, 'Abe', 61, 140000),
            (2, 'Bob', 34, 44000),
            (5, 'Chris', 34, 4000),
            (7, 'Dan', 41, 52000),
            (8, 'Ken', 57, 115000),
            (11, 'Joe', 38, 38000)
            ''')
conn.commit()

c.execute("SELECT * FROM Salesperson")
print(c.fetchall())

conn.commit()  
conn.close()
