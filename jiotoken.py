import requests
import re
import time
url = "http://thoptv.win/_livetv-jasmine/Ten3_HD-600-smumcdnems01.m3u8"
while True:
    r =requests.get(url)
    r =r.content
    a = re.split("[?\"]",r)
    token = a[2]
    b =open("token.txt","w")
    b.write(token)
    b.close()
    time.sleep(300)
