n = [5, 7, 8, 4, 1, 6, 9, 2]


def SelectionSort(arr):
    length = len(arr)
    for i in range(0, length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        # Indented inside the outer loop
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Calling the function
sorted_arr = SelectionSort(n)
print("Output:", sorted_arr)
