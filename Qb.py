# Q: c. The names of salespeople that have 2 or more orders.

import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''SELECT DISTINCT s.Name
            FROM Salesperson AS s,Customer AS c, Orders AS o
            WHERE c.Name != 'Samsonic' AND o.cust_id=c.ID and o.salesperson_id=s.ID
              ''')

print(c.fetchall())

conn.commit()
conn.close()