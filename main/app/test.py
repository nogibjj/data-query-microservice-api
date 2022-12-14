import requests


response = requests.get(url='http://127.0.0.1:8000/init/Afghanistan')
for i in response:
    print(i)
print(response)