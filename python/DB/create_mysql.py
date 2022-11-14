import mysql.connector

cnx = mysql.connector.connect(
    user='pi',
    password='pass',
    host='localhost',
    charset='utf8mb4',
)

cursor = cnx.cursor()

cursor.execute("CREATE DATABASE test")

cursor.execute("SHOW DATABASES")

cnx.close()

