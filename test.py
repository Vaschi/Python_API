import requests
import json

# Define the URL of the endpoint
url = "http://127.0.0.1:8000/"

# Create the payload
payload = {
    "name": "Chivas",
    "graphics_card": "NVIDIA",
    "cpu": "Intel i7",
    "n_of_cores": 8,
    "ram": [8, 16]
}

# Convert the payload to JSON format
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
