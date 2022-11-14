import sqlite3

db = 'data1.db'
conn = sqlite3.connect(db)
# sqliteを操作するカーソルオブジェクトを作成
cur = conn.cursor()

# SQL文
cur.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )

# データベースへコミット、変更が反映される。
conn.commit()
# データベースへのコネクションを閉じる。(必須)
conn.close()