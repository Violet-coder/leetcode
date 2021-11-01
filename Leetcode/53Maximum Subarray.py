"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:
Input: nums = [1]
Output: 1
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None

        n = len(nums)
        max_sum = -float('inf')

        # dp[i] represents the max sum end up with nums[i]
        dp = [-float('inf')] * n

        # initialization
        dp[0] = nums[0]

        # function: choose to be continuous with i - 1 or solo i
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        # answer
        return max(dp)
