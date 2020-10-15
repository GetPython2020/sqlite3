# Q: Table number contains many numbers in column num including duplicated ones.
# Can you write a SQL query to find the biggest number, which only appears once.

import sqlite3

conn = sqlite3.connect('data_L.db')
c = conn.cursor()

c.execute('''CREATE TABLE number(
           num integer)
         ''')
c.execute('''INSERT INTO number VALUES
            (1),
            (8),
            (7),
            (4),
            (1),
            (2),
            (3),
            (4),
            (8),
            (7)
            ''')

c.execute("SELECT max(num) from (SELECT num FROM number GROUP BY num Having COUNT(*)=1")
print(c.fetchall())

conn.commit()
conn.close()
