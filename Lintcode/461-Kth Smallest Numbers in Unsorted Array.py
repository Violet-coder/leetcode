"""
Find the kth smallest number in an unsorted integer array.
Example 1:
Input: [3, 4, 1, 2, 5], k = 3
Output: 3
Example 2:
Input: [1, 1, 1], k = 2
Output: 1
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
        return self.quickSelect(0, len(nums) - 1, k, nums)

    def quickSelect(self, start, end, k, nums):
        if start == end:
            return nums[start]
        i = start
        j = end
        pivot = (nums[start] + nums[end]) // 2

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
            return self.quickSelect(start, j, k, nums)
        if start + k - 1 >= i:
            return self.quickSelect(i, end, k - (i - start), nums)

        return nums[j + 1]






