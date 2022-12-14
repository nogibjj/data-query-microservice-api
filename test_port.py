import requests

# response = requests.get('http://0.0.0.0:8080/')
response = requests.get('https://wx3ucb3jpz.us-east-1.awsapprunner.com/')

print(response.json())