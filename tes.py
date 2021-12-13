import time
import requests
import serial





def serialWrite():
    a = 5
    while a > 0:
        a = a - 1
        ser = serial.Serial("/dev/pts/3")
        ser.write(b'hello \n')  
        print("ini serial \n ",a)         
        time.sleep(2)
    
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
   