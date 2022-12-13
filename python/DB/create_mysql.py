
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

try:
    txts = [f"data{i} VARCHAR(500)," for i in range(1,15)]
    txts.append("data15 VARCHAR(500)")
    sqlstate = ["CREATE TABLE smpdata(id INT,"]
    for txt in txts:
        sqlstate.append(txt)
    sqlstate.append(")")

    sqlstate = "\n".join(sqlstate)
    print(sqlstate)
    cursor.execute(sqlstate)

except mysql.connector.Error as e:
    print("error:",e)
    exit(-1)

cursor.execute("SHOW TABLES")
print(cursor.fetchall())

cnx.close()

