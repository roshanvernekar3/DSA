class Solution:

    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    # Swap adjacent elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


# Test
arr = [5, 7, 8, 4, 1, 6, 9, 2]
sol = Solution()
print("Output:", sol.bubbleSort(arr))