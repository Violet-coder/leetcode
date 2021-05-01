"""Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isValidChar(s[left]):
                left += 1
            while left < right and not self.isValidChar(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isValidChar(self, char):
        return char.isdigit() or char.isalpha()





