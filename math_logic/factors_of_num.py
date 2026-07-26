"""
Problem: Find All Factors of a Number
Time Complexity: O(N)
Space Complexity: O(K) where K is the number of factors
"""

def get_factors(n: int) -> list[int]:
    """Returns a list of all factors of integer n."""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


if __name__ == "__main__":
    # Takes custom input from the user in the terminal
    user_input = int(input("Enter a number: "))
    result = get_factors(user_input)
    print(f"Factors of {user_input} are: {result}")