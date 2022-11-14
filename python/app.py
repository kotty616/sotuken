from flask import Flask, render_template, request

app = Flask(__name__)
DATAFILE = "data.txt"

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

@app.route('/json', methods=['POST'])
def get_json():
    if 'data' in request.form:
        print(request.json)
        
if __name__ == '__main__':
    app.run(host='127.0.0.0',port=5000, debug=True)