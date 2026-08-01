# Time Complexity: O(N)  -> Scans at most N/2 character pairs
# Space Complexity: O(N) -> O(N) call stack space due to recursion depth


def is_palindrome(s, left, right):
    # Base Case: All characters matched
    if left >= right:
        return True

    # Base Case: Mismatch found
    if s[left] != s[right]:
        return False

    # Move pointers inward
    return is_palindrome(s, left + 1, right - 1)


# Driver Code
s = input("Enter a string: ")

if is_palindrome(s, 0, len(s) - 1):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
