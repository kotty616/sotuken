import requests, time, serial, sys, json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
url = 'http://127.0.0.0:5000/tmp'

def dataset(id):
    datalist = {"id":id}
    print("start")
    while True:
        if len(datalist) > 15: 
            break
        data = ser.readline().decode().replace('\r\n','')
        if data != '':
            vol = round(int(data,16)/ 1023 *5, 7)
            hosei = 28
            if vol > 0:
                # 距離*電圧=30 (2.6V*10cm=26, 1.0V*30cm=30)
                dis = round(hosei/vol, 7)
                dt_now = datetime.now()
                data = {"dis":dis, "time":dt_now.strftime("%H:%M:%S.%f")}
                datalist[f"data{len(datalist)}"] = data
                time.sleep(.5)
    # print(datalist)
    return json.dumps(datalist)

def post(data):
    r = requests.post(url, json={"data":data})
    time.sleep(3)
    print(r)


if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    
    for i in range(3):
        id = int(sys.argv[i+1])
        executor.submit(post, dataset(id))

    executor.shutdown