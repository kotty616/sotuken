import requests, time, serial
from datetime import datetime

url = 'http://127.0.0.1:5000/post'
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

def post(data):
    r = requests.post(url, data={"data": str(data)})
    time.sleep(3)
    print(r.status_code)

def read_data():
    datalist = []
    while True:   
        data = ser.readline().decode().replace('\r\n','')
        if data != '':
            vol = round(int(data)/ 1023 *5, 7)
            # 距離*電圧=30
            dis = round(28/vol, 7)
            datalist.append(dis)
        if len(datalist) > 10:
            break
    return datalist

if __name__ == '__main__':
    print(read_data())