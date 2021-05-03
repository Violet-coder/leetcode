"""
Description
Find the kth smallest number in an unsorted integer array.

Example
Example 1:

Input: [3, 4, 1, 2, 5], k = 3
Output: 3
Example 2:

Input: [1, 1, 1], k = 2
Output: 1
Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
"""


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        # write your code here
        if not nums:
            return -1

        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]

        i = start
        j = end
        pivot = nums[(i + j) // 2]

        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1

            if i <= j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1

        if start + k - 1 <= j:
            return self.quickSelect(nums, start, j, k)
        if start + k - 1 >= i:
            return self.quickSelect(nums, i, end, k - (i - start))

        return nums[j + 1]



