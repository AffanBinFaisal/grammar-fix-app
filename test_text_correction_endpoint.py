import requests
import uuid

BASE_URL = "http://127.0.0.1:8000"

def test_text_correction():
    # Generate unique user
    email = f"test_{uuid.uuid4()}@example.com"
    password = "password123"

    print(f"Testing with user: {email}")

    # 1. Register User
    print("\n1. Registering User...")
    register_url = f"{BASE_URL}/users/"
    payload = {
        "email": email,
        "password": password
    }
    try:
        response = requests.post(register_url, json=payload)
        response.raise_for_status()
        print("[OK] Registration Successful")
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] Registration Failed: {e}")
        if hasattr(e, 'response') and e.response:
             print(e.response.text)
        return

    # 2. Login
    print("\n2. Logging in...")
    login_url = f"{BASE_URL}/auth/token"
    data = {
        "username": email,
        "password": password
    }
    try:
        response = requests.post(login_url, data=data)
        response.raise_for_status()
        token_data = response.json()
        access_token = token_data["access_token"]
        print(f"[OK] Login Successful. Token: {access_token[:20]}...")
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] Login Failed: {e}")
        if hasattr(e, 'response') and e.response:
             print(e.response.text)
        return

    # 3. Test Text Correction Endpoint
    print("\n3. Testing /text-correction/ endpoint...")
    correction_url = f"{BASE_URL}/text-correction/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # Intentionally incorrect grammar
    text_payload = {
        "text": "Me no like grammar wrong."
    }
    
    try:
        response = requests.post(correction_url, json=text_payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        print("[OK] Text Correction Successful")
        print(f"Original: '{result['original_text']}'")
        print(f"Corrected: '{result['corrected_text']}'")
    except requests.exceptions.RequestException as e:
        print(f"[FAIL] Text Correction Failed: {e}")
        if hasattr(e, 'response') and e.response:
             print(e.response.text)
        return

if __name__ == "__main__":
    try:
        requests.get(BASE_URL) # Check if server is running
        test_text_correction()
    except requests.exceptions.ConnectionError:
        print("[ERROR] Error: Could not connect to the server. Is it running on http://127.0.0.1:8000?")
