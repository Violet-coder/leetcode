"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama"
Example 2:

Input: "race a car"
Output: false
Explanation: "raceacar"
"""


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here
        if s == None:
            return False

        if s == " ":
            return True

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.is_valid_char(s[left]):
                left += 1
            while left < right and not self.is_valid_char(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def is_valid_char(self, char):
        return char.isdigit() or char.isalpha()

