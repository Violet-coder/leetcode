"""
Description
Given a set of positive integers, write a function to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
Example1
Input: nums = [1, 6, 11, 5]
Output: 1
Explanation:
Subset1 = [1, 5, 6], sum of Subset1 = 12
Subset2 = [11], sum of Subset2 = 11
abs(11 - 12) = 1
Example2
Input: nums = [1, 2, 3, 4]
Output: 0
Explanation:
Subset1 = [1, 4], sum of Subset1 = 5
Subset2 = [2, 3], sum of Subset2 = 5
abs(5 - 5) = 0
"""


class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """

    def findMin(self, nums):
        # write your code here
        if not nums:
            return 0

        nums_sum = 0
        for num in nums:
            nums_sum += num

        target = nums_sum // 2
        n = len(nums)
        m = target
        dp = [[0] * (m + 1), [0] * (m + 1)]

        dp[0][0] = 0

        sum_1 = 0
        for i in range(1, n + 1):
            dp[i % 2][0] = 0
            for j in range(1, m + 1):
                if j >= nums[(i - 1)]:
                    dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - nums[(i - 1)]] + nums[(i - 1)])
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]

                if j == m:
                    sum_1 = max(sum_1, dp[i % 2][j])

        sum_2 = nums_sum - sum_1

        return abs(sum_1 - sum_2)