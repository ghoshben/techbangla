import requests
import json
import time

while True:
    url = 'https://api.jio.com/v3/dip/user/unpw/verify'
    payload = {
        "identifier": "genious.bittu1@gmail.com",
        "password": "shubham1#",
        "rememberUser": "T",
        "upgradeAuth": "Y",
        "returnSessionDetails": "T",
        "deviceInfo": {
            "consumptionDeviceName": "HUAWEI LLD-AL10",
            "info": {
                "type": "android",
                "androidId": ""
            }
        }
    }
    # Adding empty header as parameters are being sent in payload
    headers = {'Content-Type': 'application/json',
               'x-api-key': 'l7xxe10e037b4d014ed5b4df6344db3fbb01',
               'Content-Length': '290',
               'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; LLD-AL10 Build/HONORLLD-AL10)',
               'Host': 'api.jio.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    js = r.json()
    token =js["ssoToken"]
    fh =open("jio.txt","w")
    fh.write(token)
    fh.close()
    time.sleep(300)
    print("done)
