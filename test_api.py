import requests
import uuid

BASE_URL = "http://127.0.0.1:8000"

def test_auth_flow():
    # Generate unique user
    email = f"test_{uuid.uuid4()}@example.com"
    password = "password123"

    print(f"Testing with user: {email}")

    # 1. Register User
    print("\n1. Testing Registration...")
    register_url = f"{BASE_URL}/users/"
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(register_url, json=payload)
    
    if response.status_code == 200:
        print("[OK] Registration Successful")
        print(response.json())
    else:
        print(f"[FAIL] Registration Failed: {response.status_code}")
        print(response.text)
        return

    # 2. Login
    print("\n2. Testing Login...")
    login_url = f"{BASE_URL}/auth/token"
    # OAuth2PasswordRequestForm expects form data, not JSON
    data = {
        "username": email,
        "password": password
    }
    response = requests.post(login_url, data=data)
    
    if response.status_code == 200:
        print("[OK] Login Successful")
        token_data = response.json()
        access_token = token_data["access_token"]
        print(f"Access Token: {access_token[:20]}...")
    else:
        print(f"[FAIL] Login Failed: {response.status_code}")
        print(response.text)
        return

    # 3. Access Protected Route
    print("\n3. Testing Protected Route (/users/me)...")
    protected_url = f"{BASE_URL}/users/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(protected_url, headers=headers)
    
    if response.status_code == 200:
        print("[OK] Protected Route Access Successful")
        print(response.json())
    else:
        print(f"[FAIL] Protected Route Access Failed: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    try:
        requests.get(BASE_URL) # Check if server is running
        test_auth_flow()
    except requests.exceptions.ConnectionError:
        print("[ERROR] Error: Could not connect to the server. Is it running on http://127.0.0.1:8000?")
