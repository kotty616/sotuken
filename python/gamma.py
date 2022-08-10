import requests, time, serial
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
url = 'http://127.0.0.1:5000/post'

def dataset():
    data_list = []
    print("start")
    for i in range(15):            
        while True:
            if ser.in_waiting > 0:    
                dt = ser.read_all().decode().split('\r\n')
                # dt = [ds.remove('\n') for ds in dt]
                # dt = float(dt[0], 10) * 3.846
                dt = dt[0]
                dt_now = datetime.now()
                data_list.append([i+1,dt,dt_now.strftime('%H:%M:%S')])
                break

        time.sleep(.5)
    return data_list

def post(data):
    r = requests.post(url, data={"data": str(data)})
    time.sleep(3)
    print(r.status_code)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    
    for i in range(3):
        executor.submit(post, dataset())

    executor.shutdown