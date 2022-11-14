import sqlite3

db = 'data1.db'
conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute('INSERT INTO persons(name) values("Taro")')

conn.commit()

conn.close()