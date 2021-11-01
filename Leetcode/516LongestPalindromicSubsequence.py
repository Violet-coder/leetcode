"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".


Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""


# DP
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 1

        n = len(s)

        palindrome_matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            palindrome_matrix[i][i] = 1

        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                if s[i] == s[j]:
                    palindrome_matrix[i][j] = palindrome_matrix[i + 1][j - 1] + 2
                else:
                    palindrome_matrix[i][j] = max(palindrome_matrix[i + 1][j], palindrome_matrix[i][j - 1])

        return palindrome_matrix[0][n - 1]
