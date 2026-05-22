registered_users = []

for user_number in range(1, 4):
    print(f"\nRegister user {user_number}")

    name = input("Enter name: ").strip()
    email = input("Enter email: ").strip()
    dob = input("Enter date of birth: ").strip()

    user = {
        "name": name,
        "email": email,
        "dob": dob
    }

    registered_users.append(user)

print("\n===== Registered Users =====")

for number, user in enumerate(registered_users, start=1):
    print(f"\nUser {number}")
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Date of Birth: {user['dob']}")
