import requests
import json
import random
import string

BASE_URL = "http://127.0.0.1:8000/api"

def get_random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def run_test():
    username = f"user_{get_random_string(4)}"
    password = "password123"
    
    print(f"--- 1. Registering new user: {username} ---")
    reg_response = requests.post(f"{BASE_URL}/user/register/", json={
        "username": username,
        "password": password
    })
    
    if reg_response.status_code == 201:
        print("✅ Registration Successful")
    else:
        print(f"❌ Registration Failed: {reg_response.text}")
        return

    print(f"\n--- 2. Logging in to get Token ---")
    login_response = requests.post(f"{BASE_URL}/token/", json={
        "username": username,
        "password": password
    })
    
    if login_response.status_code == 200:
        token = login_response.json()['access']
        print("✅ Login Successful. Token received.")
    else:
        print(f"❌ Login Failed: {login_response.text}")
        return

    headers = {"Authorization": f"Bearer {token}"}

    print(f"\n--- 3. Creating Notes ---")
    notes_data = [
        {"title": "Note 1: Shopping List", "content": "Milk, Eggs, Bread"},
        {"title": "Note 2: Project Ideas", "content": "Mini project with Django & React"},
        {"title": "Note 3: Reminders", "content": "Call mom, pay bills"}
    ]

    for note in notes_data:
        res = requests.post(f"{BASE_URL}/notes/", json=note, headers=headers)
        if res.status_code == 201:
            print(f"✅ Created: {note['title']}")
        else:
            print(f"❌ Failed to create {note['title']}: {res.text}")

    print(f"\n--- 4. Listing Notes ---")
    list_res = requests.get(f"{BASE_URL}/notes/", headers=headers)
    if list_res.status_code == 200:
        notes = list_res.json()
        print(f"✅ Retrieved {len(notes)} notes:")
        for n in notes:
            print(f" - [{n['id']}] {n['title']}")
    else:
        print(f"❌ Failed to list notes: {list_res.text}")

    print("\n---------------------------------------------------------")
    print(f"🎉 TEST COMPLETED! You can now login on Frontend with:")
    print(f"Username: {username}")
    print(f"Password: {password}")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    try:
        run_test()
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the server is running on port 8000 and 'requests' library is installed.")
