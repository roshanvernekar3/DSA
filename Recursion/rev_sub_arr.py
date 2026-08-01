"""
Problem: Reverse Subarray
...
"""


class Solution:
    def func(self, arr, left, right):
        if left >= right:
            return

        arr[left], arr[right] = arr[right], arr[left]
        self.func(arr, left + 1, right - 1)

    def reverseSubArray(self, arr, left, right):
        self.func(arr, left - 1, right - 1)
        return arr
