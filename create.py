import random
import string

def generate_user_data(num_users):
    users = []
    for i in range(num_users):
        username = f"user{i+1:04d}"
        password = f"password{i+1:04d}"
        email = f"{username}@gmail.com"
        rollno = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        users.append({
            "username": username,
            "password": password,
            "email": email,
            "rollno": rollno
        })
    return users

user_data = generate_user_data(2000)

# Save user data to a file for reference
with open('user_data.txt', 'w') as file:
    for user in user_data:
        file.write(f"{user['username']},{user['password']},{user['email']},{user['rollno']}\n")
