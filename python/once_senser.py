import requests, time, serial,sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
url = 'http://127.0.0.0:5000/test'

def dataset(id):
    datalist = [id]
    print("start")
    while True:
        if len(datalist) == 3:
            break
        data = ser.readline().decode().replace('\r\n','')
        if data != '':
            vol = round(int(data,16)/ 1023 *5, 7)
            hosei = 28
            if vol > 0:
                dis = round(hosei/vol, 7)   # 距離*電圧=30 (2.6V*10cm=26, 1.0V*30cm=30)
                dt_now = datetime.now()
                # print(dt_now.time())
                # datalist.append([dis,dt_now.time()])
                datalist.append([dis,dt_now.strftime('%H:%M:%S.%f')])
    return datalist

def post(data):
    r = requests.post(url, data={"data":str(data)})
    time.sleep(3)
    print(r)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    id = int(sys.argv[1])
    #for i in range(3):
    executor.submit(post, dataset(id))

    executor.shutdown