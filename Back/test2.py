import requests
datas={'key1':'value1'}
r=requests.get('localhost:5000')
print(r)
d=requests.post('127.0.0.1:5000/123',data=datas)