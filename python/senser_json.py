import requests, time, serial,json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
url = 'http://127.0.0.0:5000/json'

def dataset(id):
    datalist = []
    print("start")
    while True:
        if len(datalist) >= 30: 
            break
        data = ser.readline().decode().replace('\r\n','')
        if data != '':
            vol = round(int(data,16)/ 1023 *5, 7)
            hosei = 28
            if vol > 0:
                # 距離*電圧=30 (2.6V*10cm=26, 1.0V*30cm=30)
                dis = round(hosei/vol, 7)
                dt_now = datetime.now()
                [datalist.append(i) for i in [dis,dt_now.strftime("%H:%M:%S.%f")]]
                time.sleep(.5)
                #print(len(datalist))
    dt = {"id":id, "data":datalist}
    print(type(dt))
    print(dt)
    return dt

def post(data):
    print(type(data))
    r = requests.post(url, json=data)
    time.sleep(3)
    print(r)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    id = input("idを入力してください:")
    #for i in range(3):
    executor.submit(post, dataset(id))

    executor.shutdown