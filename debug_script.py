import requests

url = "http://127.0.0.1:8000/text-correction/"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    # You might need to add Authorization header if auth is enabled
    # "Authorization": "Bearer <token>" 
}
data = {
    "text": "Me goes to store."
}

try:
    response = requests.post(url, json=data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"Request failed: {e}")
