def is_palindrome(n):
    return str(n) == str(n)[::-1]

for num in range(1, 1001):
    if is_palindrome(num):
        print(num)