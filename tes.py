import time
import requests
import serial
import json

def serialWrite():
    try :
        ser = serial.Serial("/dev/pts/3")
        print ('serial open')
        a=7 
        while a > 0 :
            a = a-1
            ser.write(b'1\n')
            print("writing",a)
            time.sleep(1) 
        # write api to 0
        try : 
            data = {"nomor": "1","status": "0"}
            headers = {"Content-Type": "application/json"}
            r = requests.put("http://client666.pythonanywhere.com/beautycare/apicopi/status/1/", data=json.dumps(data), headers=headers)
            print("habis time")
            res = r.json()
            print("result PUT =",res)
        except :
            print ('tidak terkirim', r)
        ser.close()
        test()

    except :
        print("serial not connexted")
        # send to api error serial 
        data = {"nomor": "1","status": "0"}
        headers = {"Content-Type": "application/json"}
        r = requests.put("http://client666.pythonanywhere.com/beautycare/apicopi/status/1/", data=json.dumps(data), headers=headers)
        resp = r.json()
        print(resp)
        test()

def test() :
    t = 9
    while t > 1:
        t = t -1
        # print(t)
        try:
            # response = requests.get("https://reqres.in/api/users/3")
            response = requests.get("http://client666.pythonanywhere.com/beautycare/apicopi/status/?format=json")
            responseJson = response.json()
            print (responseJson[0]["status"])
            value = responseJson[0]["status"]
            # value = "s"
            if value == "1" : 
                t = 0    
                serialWrite()
            else :
                t = 9
            # time.sleep(1)
        except (requests.ConnectionError, requests.Timeout) as exception:
            t = 9
            print("No internet connection.")
        time.sleep(0.3)

test() 
   