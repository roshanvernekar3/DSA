n = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def func(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left + 1, right - 1)


func(n, 0, len(n) - 1)
print("Reversed array:", n)
