"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
Example 1:
Input:"abcdzdcab"
Output:"cdzdc"
Example 2:
Input:"aba"
Output:"aba"
"""


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""

        answer = (0, 0)  # use tuple to record(palindrome length, start char)

        for middle in range(len(s)):
            answer = max(answer, self.getPalindromeFromTheMiddle(s, middle, middle))
            answer = max(answer, self.getPalindromeFromTheMiddle(s, middle, middle + 1))

        return s[answer[1]: answer[1] + answer[0]]

    def getPalindromeFromTheMiddle(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 1, left + 1)


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""

        n = len(s)
        answer = (0, "")

        for i in range(n):
            answer = max(answer, self.palindromic_substring_based_middle(s, i - 1, i + 1))
            answer = max(answer, self.palindromic_substring_based_middle(s, i, i + 1))

        return answer[1]

    def palindromic_substring_based_middle(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break

        return (right - left - 1, s[left + 1: right])