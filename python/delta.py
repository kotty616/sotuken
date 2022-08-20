import requests, time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

url = 'http://127.0.0.1:5000/post'

def dataset(id):
    data_list = []
    print("start")
    for i in range(15):            
        while True:
                dt = i+1
                dt_now = datetime.now()
                data_list.append([id,dt,dt_now.strftime('%H:%M:%S')])
                break

        time.sleep(.5)
    return data_list

def post(data):
    r = requests.post(url, data={"data": str(data)})
    time.sleep(3)
    print(r.status_code)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    id = input('IDを入力してください')
    for i in range(1):
        executor.submit(post, dataset(id))

    executor.shutdown