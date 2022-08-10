from flask import Flask, render_template, request, redirect

app = Flask(__name__)
DATAFILE = "data.txt"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post', methods=['POST'])
def get_data():
    if 'data' in request.form:
        data = str(request.form['data'])
        with open(DATAFILE, 'a') as f:
            f.write(data)
            f.write('\n')
            print(data)
    else:
        print('Not data')
    return "None"

if __name__ == '__main__':
    app.run(debug=True)