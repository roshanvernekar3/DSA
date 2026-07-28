# Using Recursion to check if a string is a palindrome

def is_palindrome(s, left, right):
    if left >= right:
        return True

    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)

s = input("Enter a string: ")

if is_palindrome(s, 0, len(s) - 1):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")