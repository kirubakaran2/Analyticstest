import random
import string

def generate_user_data(num_users, start_index=1):
    users = []
    for i in range(start_index, start_index + num_users):
        username = f"user{i:04d}"
        password = f"password{i:04d}"
        email = f"{username}@gmail.com"
        rollno = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        users.append({
            "username": username,
            "password": password,
            "email": email,
            "rollno": rollno
        })
    return users

# Generate the initial 2000 users
user_data_1 = generate_user_data(2000, start_index=1)

# Save the initial 2000 user data to a file for reference
with open('user_data_initial.txt', 'w') as file:
    for user in user_data_1:
        file.write(f"{user['username']},{user['password']},{user['email']},{user['rollno']}\n")

# Generate an additional 2000 users
user_data_2 = generate_user_data(2000, start_index=2001)

# Save the additional 2000 user data to a separate file for reference
with open('user_data_additional.txt', 'w') as file:
    for user in user_data_2:
        file.write(f"{user['username']},{user['password']},{user['email']},{user['rollno']}\n")
