"""
Description
Give n items and an array, num[i] indicate the size of ith item. An integer target denotes the size of backpack. Find the number of ways to fill the backpack.

Each item may be chosen unlimited number of times
Example1

Input: nums = [2,3,6,7] and target = 7
Output: 2
Explanation:
Solution sets are:
[7]
[2, 2, 3]
Example2

Input: nums = [2,3,4,5] and target = 7
Output: 3
Explanation:
Solution sets are:
[2, 5]
[3, 4]
[2, 2, 3]
"""


class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """

    def backPackIV(self, nums, target):
        # write your code here
        # dp[i] 前n个数组成和为i的方案数
        # i 0 => target 一共target+1个

        if not nums:
            return 0

        n = len(nums)
        m = target

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, m + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - nums[i - 1]]
                    # count = j // nums[i - 1]
                    # for k in range(0, count + 1):
                    #     dp[i][j] += dp[i - 1][j - k * nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]



