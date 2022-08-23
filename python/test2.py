import requests, time, sys,serial
from datetime import datetime

url = 'http://127.0.0.1:5000/post'
ser = serial.Serial("/dev/cu.usbmodem142101", 9600, timeout=1)

def post(data):
    r = requests.post(url, data={"data": str(data)})
    time.sleep(3)
    print(r.status_code)

def read_data():
    datalist = []
    for i in range(10):    
        while True:
            if ser.in_waiting > 0:
                data = ser.read_all().decode().split('\r\n')
                datalist.append(data)
                break
    return datalist

if __name__ == '__main__':
    print(read_data())