"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.
Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
"""


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        n = len(nums)
        nums.sort()

        # state: dp[i]表示以nums[i]结尾的largestDivisibleSubset最长长度
        # initializaion: dp[0, ...., n-1] = 1
        dp = [1] * n

        # prev[i]代表dp[i]的最优值是从哪个dp[j]算过来的
        prev = [-1] * n

        # function dp[i] = max(dp[i], dp[j] + 1)  nums[i] % nums[j] == 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        longest = 0
        last = -1

        # answer: max(dp[0,...,n-1])
        for i in range(n):
            if dp[i] > longest:
                longest = dp[i]
                last = i

        print("longest", longest)
        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]

        return path[::-1]
