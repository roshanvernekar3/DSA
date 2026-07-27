"""
Problem: Reverse Subarray

Difficulty: Basic

Question:
Given an array `arr`, reverse a subarray of that array. The range of this
subarray is given by indices `l` and `r` (1-based indexing).

Examples:

Input:
arr = [1, 2, 3, 4, 5, 6, 7]
l = 2, r = 4

Output:
[1, 4, 3, 2, 5, 6, 7]

Explanation:
After reversing the elements in the range 2 to 4 (2, 3, 4),
the modified array becomes [1, 4, 3, 2, 5, 6, 7].

Input:
arr = [1, 6, 7, 4]
l = 1, r = 4

Output:
[4, 7, 6, 1]

Explanation:
After reversing the elements in the range 1 to 4,
the modified array becomes [4, 7, 6, 1].

Constraints:
1 ≤ arr.size() ≤ 10^6
1 ≤ arr[i] ≤ 10^6
1 ≤ l ≤ r ≤ arr.size()

Approach:
- Convert the given 1-based indices to 0-based indices.
- Use recursion with two pointers.
- Swap the left and right elements.
- Continue until the pointers meet.

Time Complexity: O(r - l + 1)
Space Complexity: O(r - l + 1) (recursive stack)
"""


class Solution:
    def func(self, arr, l, r):
        if l >= r:
            return

        arr[l], arr[r] = arr[r], arr[l]
        self.func(arr, l + 1, r - 1)

    def reverseSubArray(self, arr, l, r):
        self.func(arr, l - 1, r - 1)
        return arr
