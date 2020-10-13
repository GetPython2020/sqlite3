import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

#c.execute("DROP TABLE Orders")
#conn.commit()

# only run one time
#c.execute(''' CREATE TABLE Orders (
#            Number integer,
 #           order_date text,
  #          cust_id integer,
   #         salesperson_id integer,
    #        Amount integer)
     #  ''')

c.execute("DELETE FROM Orders")
conn.commit()

#only run one time
c.execute('''INSERT INTO Orders VALUES
            (10,'8/2/96',4,2,540),
            (20,'1/30/99',4,8,1800),
            (30,'7/14/95',9,1,460),
            (40,'1/29/98',7,2,2400),
            (50,'2/3/98',6,7,600),
            (60,'3/2/98',6,7,720),
            (70,'5/6/98',6,7,150)
              ''')
conn.commit()

c.execute("SELECT * FROM Orders")
print(c.fetchall())

conn.commit()  # execute the sql command
conn.close()