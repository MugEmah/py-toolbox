
# def greet_names(names):
#     for name in names:
#         greeting = f"Welcome, {name}! Nice to meet you."
#         print(greeting)

# # Output
# greet_names(["Emma", "Hope", "Mike"])

# def area_of_the_rectangle(length, width):
#     return length * width

# print(area_of_the_rectangle(5, 10))

# def product_of_five(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product % 5 == 0

# print(product_of_five([1, 2, 5])) 
# print(product_of_five([1, 2, 3])) 

# path = f"/home/emah/Desktop/Python project"

# print(path)

# value = input("Enter a value: ")

# In Python, input() always returns a string.
# This verifies that the entered value is indeed a string object.
# if isinstance(value, str):
#     print(f"Input is a string: {value!r}")
#     if value.isdigit():
#         print("The entered value contains only digits, but it is still a string.")
# else:
#     print("The input is not a string.")

# days_of_week = "weekend" if day.upper() in ["Saturday", "Sunday"] else "weekday"

# print(days_of_week)


# try:
#     num1 = float(input("Enter first number: "))
#     op = input("Enter operator (+, -, *, /): ")
#     num2 = float(input("Enter second number: "))

#     if op == '+':
#         print(num1 + num2)
#     elif op == '-':
#         print(num1 - num2)
#     elif op == '*':
#         print(num1 * num2)
#     elif op == '/':
#         if num2 == 0:
#             print("Error: Cannot divide by zero")
#         else:
#             print(num1 / num2)
#     else:
#         print("Invalid operator")

# except ValueError:
#     print("Error: Use numbers only")





# username = input("Username: ")
# password = input("Password: ")

# if username == "admin" and password == "pass123":
#     print("Access Granted")
# else:
#     print("Access Denied")


# import random 

# pick a random integer btn 0 - 100
# random_number = random.randint(1, 100)
# attempts = 0
# print(random_number)
# while loop that terminates if the user input == random number selected by the pc
# while True:
#     attempts += 1
#     # if user input == selected by pc : break out of the loop
#     try:
#         user_input = int(input("Guess the number btn 1 - 100: "))
#         if user_input == random_number:
#             print(f"Bingo, You Got The Number Right: {user_input} in {attempts} attempts")
#             break
#         elif user_input < random_number:
#             print(f"Too low!, Try a higher number.")
#         else:
#             print(f"Too high!, Try a lower number.")
#     except ValueError as e:
#         print(f"Error: {e}")
# # Modify the program to guide the user into getting 
# # the random number in the shortest number of attempts


# msg = "We are happy for you"

# # Using find() to locate the starting position of "happy"
# start = msg.find("happy")
# # Calculate the ending
# end = start + len("happy")
# # Use slicing to extract "happy"
# print(msg[7:12])

# msg = "Hello mercy, How are you today?"

# msg = msg.isupper()
# print(msg)

# def check_p(text):
#     word_lower = text.lower().replace(" ", "")
#     return word_lower == word_lower[::-1]

# print(check_p("omo"))

# msg = "Python Programming"

# print(msg[:6])
# print(msg[7:])
# print(msg[0:18:2])

# mynames = ["David", "Emmanuel", "Mercy", "etc"]
# remove_names = ["Mercy", "Emmanuel"]
# for name in remove_names:
#     while name in mynames:
#         mynames.remove(name)

# print(mynames)

# info = [['Dave', 'Mercy'], ['Peace', 'Ema']]

# # for sublist in info:
# #     for name in sublist:
# #         print(name)

# info1 = [name for list1 in info for name in list1]
# print(info1)

# students = []


# def show_menu():
#     print("\n===== Student Menu =====")
#     print("1. Add Student")
#     print("2. List Students")
#     print("3. Delete Student")
#     print("4. Exit")


# def add_students():
#     print("\nAdd students one at a time.")
#     print("Type q when you are done.")

#     while True:
#         name = input("Enter student name: ").strip()

#         if name.lower() == "q":
#             print("Finished adding students.")
#             break

#         if name == "":
#             print("Student name cannot be empty.")
#             continue

#         students.append(name)
#         print(f"{name} has been added.")


# def list_students():
#     print("\n===== Student List =====")

#     if len(students) == 0:
#         print("No students have been added yet.")
#         return

#     for number, student in enumerate(students, start=1):
#         print(f"{number}. {student}")


# def delete_student():
#     if len(students) == 0:
#         print("\nNo students to delete.")
#         return

#     name = input("\nEnter the student name to delete: ").strip()

#     if name in students:
#         students.remove(name)
#         print(f"{name} has been deleted.")
#     else:
#         print(f"{name} was not found.")


# print("Welcome to the Student Management Program!")

# while True:
#     show_menu()
#     choice = input("Choose an option 1-4: ").strip()

#     if choice == "1":
#         add_students()
#     elif choice == "2":
#         list_students()
#     elif choice == "3":
#         delete_student()
#     elif choice == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please choose 1, 2, 3, or 4.")


# numbers = [3, 4, 0, 0, 0, 6, 2, 8, 7, 6, 0, 0, 0, 9, 10, 2, 0, 0, 6, 4, 5, 0, 0, 4, 9, 11, 0, 0, 55, 2, 0, 0, 36, 5, 8]

# def move_zeros_to_end(numbers):
#     non_zero_numbers = []
#     zeros = []

#     for number in numbers:
#         if number == 0:
#             zeros.append(number)
#         else:
#             non_zero_numbers.append(number)

#     return non_zero_numbers + zeros


# result = move_zeros_to_end(numbers)

# print(numbers)
# print(result)

registered_users = []

for user_number in range(1, 4):
    print(f"\nRegister user {user_number}")

    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    dob = input("Enter your date of birth: ").strip()

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