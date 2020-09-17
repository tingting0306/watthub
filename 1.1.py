import requests
url='http://192.168.1.7:8081/login'
body={
         "name":"admin",
         "password":"123456"
     }
res=requests.post(url=url,json=body)
print(res.text)