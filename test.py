import requests
import json

# URL of the endpoint
url = 'http://localhost:3001/authenticate'  # Replace with your actual URL

# Payload to be sent in the POST request
payload = {
    'username': 'yufan',
}

# Headers
headers = {
    'Content-Type': 'application/json'
}

# Making the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
print(f'Status Code: {response.status_code}')
print(f'Response Body: {response.text}')
print("test")
print("tilt")
print("tilt")
print("tilt")
print("tilt")
print("tilt")
print("tilt")
print("tilt")
print("tilt")
print("tilt")
