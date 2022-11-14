import requests, time
from datetime import datetime

url = 'http://127.0.0.1:5000/post'

def dataset():
    data_list = []
    for i in range(15):                
        dt_now = datetime.now()
        dt = i
        data_list.append([dt,dt_now.strftime('%H:%M:%S')])

        time.sleep(.5)
        
    return data_list

def post(data):
    r = requests.post(url, data={"data": str(data)})
    print(r.status_code)

if __name__ == '__main__':
    post(dataset())