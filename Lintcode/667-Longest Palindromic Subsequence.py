"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
Example1
Input: "bbbab"
Output: 4
Explanation:
One possible longest palindromic subsequence is "bbbb".
Example2
Input: "bbbbb"
Output: 5
"""


class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """

    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0

        n = len(s)
        #dp[i][j] s[i...j] 从i到j的substring最长回文串的长度
        #base case: dp[i][i] = 1
        #case 1: s[i] == s[j] dp[i][j] = dp[i + 1][j - 1] + 2
        #case 2: s[i] != s[j] dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return dp[0][n - 1]

