import mysql.connector

class Mysql:
    def __init__(self, config) -> None:
        self.conn_db(config)
        
    def _close(self):
        if self.conn.is_connected():
            return "NONE"
        self.cur.close()

    def conn_db(self, config):
        self.conn = mysql.connector.connect(**config)
        if not self.conn.is_connected():
            return -1
        return self.cursor()
    
    def cursor(self):
        self.cur = self.conn.cursor()
    
    def insert_db(self, datadict):
        id = datadict.pop("id")
        for data in datadict.values():
            quely = 'INSERT INTO datalist VALUES({0},"{2}",{1});'.format(id,*data.values())
            self.cur.execute(quely)
        self.conn.commit()

    def show_db(self):
        quely = "SELECT DISTINCT id FROM datalist ORDER BY id;"
        self.cur.execute(quely)
        ids = self.cur.fetchall()   #[(id),(id),...]の形式になっている
        for id in ids:
            print(id[0])    #idはtupleなので要素を取り出す必要あり
            quely = f"SELECT * FROM datalist WHERE id={id[0]};"
            self.cur.execute(quely)
            for fet in self.cur.fetchall():
                print(fet)

if __name__ == "__main__":
    config = {
        "user":'pi',
        "host":'localhost',
        "password":'pass',
        "database":'sotuken'
    }
    
    sql = Mysql(config)
    sql.show_db()
    sql._close()