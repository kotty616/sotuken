import  serial
from datetime import datetime

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

def read_data():
    datalist = []
    while True:   
        data = ser.readline().decode().replace('\r\n','')
        if data != '':
            datalist.append(int(data,16))
        if len(datalist) > 10:
            break
    return datalist

if __name__ == '__main__':
    data = read_data()
    print(data)
    with open("dataset.txt", 'a') as f:
        f.write("30:")
        f.write(str(data))
        f.write('\n')