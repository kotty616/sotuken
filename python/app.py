from flask import Flask, render_template, request
import json
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
        id = datadict.pop("id")
        for data in datadict.values():
            quely = 'INSERT INTO datalist VALUES({0},"{2}",{1});'.format(id,*data.values())
            self.cur.execute(quely)
        self.conn.commit()

    def show_db(self):
        quely = f"SELECT * FROM datalist"
        self.cur.execute(quely)
        for fet in self.cur.fetchall():
            print(fet)

app = Flask(__name__)
config = {
    "user":'pi',
    "host":'localhost',
    "password":'pass',
    "database":'sotuken'
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tmp', methods=["POST"])
def get_text():
    d = request.get_json()["data"]
    d = json.loads(d)

    mysql = Mysql(config)
    mysql.insert_db(d)
    mysql.show_db()

    return 'NONE'

if __name__ == '__main__':
    app.run(host='127.0.0.0',port=5000, debug=True)

@app.route('/test', methods=['POST'])
def get_test():
    if 'data' in request.form:
        data = request.form.get("data").replace("[","").replace("]","")
        data = data.split(",")
        id = 0
        time = []
        dis = []
        for i,d in enumerate(data):
            if i == 0:
                id = int(d)
            elif i%2 != 0:
                dis.append(float(d))
            else:
                d = d.replace("'","").replace(" ","")
                print(d)
                time.append('"'+d+'"')
    return "None"

# @app.route('/post', methods=['POST'])
# def get_data():
#     if 'data' in request.form:
#         data = request.form.get('data')
#         #print(list(data))
#         with open(DATAFILE, 'a') as f:
#             f.write(data)
#             f.write('\n')
#     else:
#         print('Not data')
#     return "None"

"""
def conn_db():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'pi',
        password = 'pass',
        database = 'sotuken'
    )
    return conn

def insert_datalist(cur, id, dis, time):
    sql = f"INSERT INTO datalist VALUES({id}, {time}, {dis});"
    print(sql)
    cur.execute(sql)

def json_insert(cur,dic):
    quely = "INSERT INTO smpdata VALUES("
    for i,data in enumerate(dic.values()):
        if i == 0:
            quely = quely + str(data)
        else:
            quely += '"'+str(data)+'"'
        if i != len(dic)-1:
            quely += ","
    quely = quely + ");"
    print(quely)
    cur.execute(quely)
    
def show_db(cur, datalist):
    sql = f"SELECT * FROM {datalist};"
    cur.execute(sql)
    for fet in cur.fetchall():
        print(fet)
"""