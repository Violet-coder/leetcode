"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        alphabet_dict = {}
        longest_palindrome_length = 0
        odd_times = 0

        # build the dict to count the number of each char
        for char in s:
            alphabet_dict[char] = alphabet_dict.get(char, 0) + 1

        for key in alphabet_dict.keys():
            # if the amount of the char is odd, use the even part to contribute to the palindrome
            if alphabet_dict[key] % 2:
                longest_palindrome_length += alphabet_dict[key] - 1
                odd_times += 1

            else:
                longest_palindrome_length += alphabet_dict[key]

        if odd_times:
            longest_palindrome_length += 1

        return longest_palindrome_length



