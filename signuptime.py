import requests
import json
import concurrent.futures
import urllib3
import time

# Suppress only the single InsecureRequestWarning from urllib3 needed
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

signup_url = "https://51.20.235.124/admin/colleges/66518458601ea24504e7741f/665279ae49b21b4dd49fd272/add"
bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NDE5NzkyNjcxYzkxYmRjZDhmOGFkNSIsIm5hbWUiOiJBZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4iLCJpYXQiOjE3MTg4ODk3NTUsImV4cCI6MTcxODk3NjE1NX0.vI3DWBDG8UqjgAHjt1RB21jBbqqc9DzgZXEbrXTY8Dw"

def signup_user(user):
    payload = {
        "users": [{
            "name": user['username'],
            "username": user['username'],
            "password": user['password'],
            "email": user['email'],
            "rollno": user['rollno'],
            "role": "student"
        }]
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.post(signup_url, data=json.dumps(payload), headers=headers, verify=False)
    return response.text

def main():
    start_time = time.time()

    with open('user_data_additional.txt', 'r') as file:
        user_data = [line.strip().split(',') for line in file]

    users = [
        {"username": data[0], "password": data[1], "email": data[2], "rollno": data[3]}
        for data in user_data
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(signup_user, user) for user in users]
        with open('signup2_responses.txt', 'w') as file:
            for future in concurrent.futures.as_completed(futures):
                file.write(future.result() + "\n")

    end_time = time.time()
    duration = end_time - start_time
    print(f"Total signup time for {len(users)} users: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
