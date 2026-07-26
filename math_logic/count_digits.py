n = int(input("Enter a number: "))
COUNT = 0
while n > 0:
    COUNT += 1
    n = n // 10
print("Number of digits:", COUNT)
