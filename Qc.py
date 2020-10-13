# Q: c. The names of salespeople that have 2 or more orders.

import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''SELECT s.Name
            FROM Salesperson AS s,Orders AS o
            WHERE o.salesperson_id=s.ID
            GROUP BY o.salesperson_id
            HAVING COUNT(*)>=2
              ''')

print(c.fetchall())

conn.commit()
conn.close()