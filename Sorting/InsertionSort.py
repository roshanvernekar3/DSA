arr = [5, 7, 8, 4, 1, 6, 9, 2]

def insertionSort(arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            
            arr[j+1] = key
            
        return arr
        
sorted_nums = insertionSort(arr)
print("Output:", sorted_nums)
                