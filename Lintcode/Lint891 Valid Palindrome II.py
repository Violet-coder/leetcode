"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
The string will only contain lowercase characters.
The maximum length of the string is 50000.
Example 1:
Input: s = "aba"
Output: true
Explanation: Originally a palindrome.
Example 2:
Input: s = "abca"
Output: true
Explanation: Delete 'b' or 'c'.
Example 3:
Input: s = "abc"
Output: false
Explanation: Deleting any letter can not make it a palindrome.
"""


class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """

    def validPalindrome(self, s):
        # Write your code here
        n = len(s)
        left, right = self.find_difference(s, 0, n - 1)
        if left >= right:
            return True
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)

    def find_difference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right

    def is_palindrome(self, s, left, right):
        left, right = self.find_difference(s, left, right)
        return left >= right
