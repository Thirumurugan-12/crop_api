import requests
import json

# The URL of your Flask API
url = 'http://localhost:5000/predict'

# The data you want to send to the API for prediction
data = {'input': [6,5,7,36.6667,42.12345,20.678,10.3245]}

# Send the POST request to the API
response = requests.post(url, json=data)

# Check the status code
print('Status code:', response.status_code)

# Print out the response
if response.text:
    print(response.json())
else:
    print('Empty response')