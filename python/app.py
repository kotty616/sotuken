from flask import Flask, render_template, request, jsonify
import mysql.connector 
import json

app = Flask(__name__)
DATAFILE = "data/data.txt"

def conn_db():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'pi',
        password = 'pass',
        database = 'sotuken'
    )
    return conn

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post', methods=['POST'])
def get_data():
    if 'data' in request.form:
        data = request.form.get('data')
        #print(list(data))
        with open(DATAFILE, 'a') as f:
            f.write(data)
            f.write('\n')
    else:
        print('Not data')
    return "None"

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
                time.append(d.replace("'","").replace(" ",""))
        
    return "None"

@app.route('/tmp', methods=["POST"])
def get_text():
    d = request.get_json()["data"]
    # d = json.dumps(d)
    d = dict(d)
    print(d)
    # with open("tmp.txt", "a") as f:
    #     f.write('\n')
    #     f.write()
    # if 'data' in request.form:    
    #     data = request.form.get("data")
    #     with open(DATAFILE, 'a') as f:
    #         f.write('\n')
    #         f.write(data)
    return 'NONE'

if __name__ == '__main__':
    app.run(host='127.0.0.0',port=5000, debug=True)