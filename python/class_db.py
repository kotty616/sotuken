import mysql.connector

class Mysql:
    def __init__(self, config) -> None:
        self.conn_db(config)
        
    def __del__(self):
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
        quely = "INSERT INTO smpdata VALUES("
        for i,data in enumerate(datadict.values()):
            if i == 0:
                quely += str(data)
            else:
                quely += '"'+str(data)+'"'
            if i != len(datadict)-1:
                quely += ","
        quely += ");"
        self.cur.execute(quely)
        self.conn.commit()

    def show_db(self):
        quely = f"SELECT * FROM smpdata"
        self.cur.execute(quely)
        for fet in self.cur.fetchall():
            print(fet)