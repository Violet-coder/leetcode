"""
Description
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
Return the absolute value of difference between the sum of the two numbers and the target.
Example1
Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).
Example2

Input:  nums = [-1, -1, -1, -4] and target = 4
Output: 6
Explanation:
The minimum difference is 6. (4 - (- 1 - 1) = 6).
"""


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """

    def twoSumClosest(self, nums, target):
        # write your code here
        max_value = float('inf')
        if not nums:
            return max_value

        diff = max_value

        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                diff = 0
                return diff
            elif total < target:
                diff = min(diff, abs(total - target))
                left += 1
            else:
                diff = min(diff, abs(total - target))
                right -= 1

        return diff



