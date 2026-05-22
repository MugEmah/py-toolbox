value = input("Enter a value: ")

# In Python, input() always returns a string.
# This verifies that the entered value is indeed a string object.
if isinstance(value, str):
    print(f"Input is a string: {value!r}")
    if value.isdigit():
        print("The entered value contains only digits, but it is still a string.")
else:
    print("The input is not a string.")
