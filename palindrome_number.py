def is_palindrome_number(number):
    text = str(number)
    return text == text[::-1]


num = input("Enter a number: ")

if is_palindrome_number(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
