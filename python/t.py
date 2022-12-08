import requests,json

url = 'http://127.0.0.0:5000/tmp'
data = json.dumps({
    "id":1,
    "data1":{"dis":10,
            "time":"10:10"
            },
    "data2":{"dis":10,
            "time":"10:10"
    },
    "data3":{"dis":10,
    "time":"10:10"
    }
})

r = requests.post(url, data={"data":data})