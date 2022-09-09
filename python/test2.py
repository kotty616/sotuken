import requests, time, sys,serial
from datetime import datetime

# dev = "/dev/cu.usbmodem142101"
dev = "/dev/cu.usbmodem141101"

url = 'http://127.0.0.1:5000/post'
ser = serial.Serial(dev, 9600, timeout=1)

def post(data):
    r = requests.post(url, data={"data": str(data)})
    time.sleep(3)
    print(r.status_code)

def read_data():
    datalist = []
    data = ''
    data = ser.read_all()
    for i in range(10):    
        while True:
            if ser.in_waiting > 0:
                data = ser.read_all().decode().split('\r\n')
                datalist.append(data)
                break
    return datalist

if __name__ == '__main__':
    print(read_data())