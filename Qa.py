# Q: a. The names of all salespeople that have an order with Samsonic.

import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''SELECT s.Name
            FROM Salesperson AS s, Customer AS c,Orders AS o
            WHERE c.Name = 'Samsonic' AND o.cust_id=c.ID and o.salesperson_id=s.ID
              ''')

print(c.fetchall())

conn.commit()  # execute the sql command
conn.close()