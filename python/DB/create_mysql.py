
import mysql.connector  # 何故かver=8.0.29でないと動かない

config = {
    "user":"pi",
    "password":"pass",
    "host":"localhost",
    "database":"sotuken"  
}
try:
    cnx = mysql.connector.connect(**config)
    print(cnx.is_connected())
    
except mysql.connector.Error as e:
    print("error:",e)
    exit(-1)

cursor = cnx.cursor()

sqlstate = """
CREATE TABLE datalist(
    id INT,
    time DATE,
    dis FLOAT
);
"""
cursor.execute(sqlstate)

cursor.execute("SHOW TABLES")
print(cursor.fetchall())

cnx.close()

