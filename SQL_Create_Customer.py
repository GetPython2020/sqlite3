import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

# only run one time
c.execute(''' CREATE TABLE Customer (
            ID integer,
            Name text,
            City text,
            Industry Type text)
       ''')

c.execute("DELETE FROM Customer")
conn.commit()

#only run one time
c.execute('''INSERT INTO Customer VALUES
            (4, 'Samsonic','pleasant','J'),
            (6, 'Panasung','oaktown','J'),
            (7, 'Samony','jackson', 'B'),
            (9, 'Orange','Jackson','B')
              ''')
conn.commit()

c.execute("SELECT * FROM Customer")
print(c.fetchall())

conn.commit()  # execute the sql command
conn.close()