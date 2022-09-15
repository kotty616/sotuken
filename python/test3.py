import requests, time, serial
from datetime import datetime

url = 'http://localhost:5000/post'
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
            hosei = 28
            # 距離*電圧=30(2.6V*10cm=26, 1.0V*30cm=30)
            dis = round(hosei/vol, 7)
            datalist.append(dis)
        if len(datalist) > 10:
            break
    return datalist

if __name__ == '__main__':
    data =read_data()
    print(read_data())
    post(data)