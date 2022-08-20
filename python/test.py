import requests, time, sys
from datetime import datetime

url = 'http://127.0.0.1:5000/post'

def post(data):
    r = requests.post(url, data={"data": str(data)})
    time.sleep(3)
    print(r.status_code)

if __name__ == '__main__':
    while 1:
        data = [sys.argv[1],datetime.now().strftime('%H:%M:%S')]
        post(data)
        time.sleep(2)