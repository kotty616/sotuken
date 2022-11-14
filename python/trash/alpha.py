import requests, time, serial
from datetime import datetime

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
url = 'http://127.0.0.1:5000/post'

def dataset():
    data_list = []
    for i in range(15):            
        while True:
            if ser.in_waiting > 0:    
                dt_now = datetime.now()
                dt = ser.read_all().decode().rstrip('\r\n').split('\r\n')
                if dt[0] != '':
                    dt = int(dt[0], 16)
                else:
                    dt = int(dt[1], 16)
                data_list.append([i+1,dt,dt_now.strftime('%H:%M:%S')])
                break

        time.sleep(.5)
    return data_list

def post(data):
    r = requests.post(url, data={"data": str(data)})
    print(r.status_code)

if __name__ == '__main__':
    post(dataset())