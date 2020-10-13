# Q: d. Write a SQL statement to insert rows into a table called highAchiever(Name, Age),
# where a salesperson must have a salary of 100,000 or greater to be included in the table.

import sqlite3 

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''CREATE TABLE highAchiever
            ( Name text,
              Age integer
            )''')

c.execute('''INSERT INTO highAchiever
            SELECT Name, Age FROM Salesperson
            WHERE Salary >= 100000
              ''')

c.execute('SELECT * FROM highAchiever')
print(c.fetchall())

conn.commit()
conn.close()
