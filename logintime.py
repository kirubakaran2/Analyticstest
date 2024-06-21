import requests
import json
import concurrent.futures
import urllib3
import time

# Suppress warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

login_url = "https://51.20.235.124/login"
num_users = 2000
user_data_file = 'user_data.txt'
login_responses_file = 'login2_responses.txt'

# Read user data from file
def read_user_data(file):
    with open(file, 'r') as f:
        user_data = [line.strip().split(',') for line in f]
    return [{"username": data[0], "password": data[1]} for data in user_data]

users = read_user_data(user_data_file)

# Function to login a user
def login_user(user):
    payload = {
        "username": user['username'],
        "password": user['password']
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(login_url, data=json.dumps(payload), headers=headers, verify=False)
    return response.status_code, response.text

# Run the login test
def main():
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(login_user, user) for user in users]
        
        results = []
        for future in concurrent.futures.as_completed(futures):
            status, response_text = future.result()
            results.append(f"Status: {status}, Response: {response_text}")
        
        # Write all responses to the file at once
        with open(login_responses_file, 'w') as file:
            for result in results:
                file.write(result + "\n")

    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Total login time for {num_users} users: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
