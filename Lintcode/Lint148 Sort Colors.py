"""
Description
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

You are not suppose to use the library's sort function for this problem.
You should do it in-place (sort numbers in the original array).
You are not allowed to use counting sort to solve this problem.

Example
Example 1

Input : [1, 0, 1, 2]
Output : [0, 1, 1, 2]
Explanation : sort it in-place
Challenge
Could you come up with an one-pass algorithm using only O(1) space?
"""

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    def sortColors(self, nums):
        # write your code here
        if not nums:
            return []

        n = len(nums)

        zero_boundary = self.partition(nums, 0, n - 1, 1)
        self.partition(nums, zero_boundary, n - 1, 2)

        return nums

    def partition(self, nums, start, end, pivot):
        left = start
        right = end

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

