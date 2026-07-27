n = [5, 2, 8, 5, 1, 9, 2, 5, 7, 8]
m = [3, 6, 3, 1, 9, 6, 4, 2, 3, 7, 9, 1]

for num in m:
    count = 0
    for x in n:
        if x == num:
            count += 1

print(f"Frequency of {num} in n is: {count}")
