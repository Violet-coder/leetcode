"""
Description
Given n items with size nums[i] which an integer array and all positive numbers. An integer target denotes the size of a backpack. Find the number of possible fill the backpack.
Each item may only be used once
Example
Given candidate items [1,2,3,3,7] and target 7,
A solution set is:
[7]
[1, 3, 3]
return 2
"""


class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """

    def backPackV(self, nums, target):
        # write your code here
        # dp[i] 前n个数组成和为i的方案数
        # i 0 => target 一共target+1个

        if not nums:
            return 0

        n = len(nums)
        m = target

        dp = [[0] * (m + 1), [0] * (m + 1)]

        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i % 2][0] = 1
            for j in range(1, m + 1):
                if j >= nums[i - 1]:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[(i - 1) % 2][j - nums[i - 1]]
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]

        return dp[n % 2][target]