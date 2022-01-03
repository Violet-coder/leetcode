"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Example 1:
Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
"""


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return 0

        alpha_dict = {}
        has_ood_times = 0
        result = 0

        for char in s:
            alpha_dict[char] = alpha_dict.get(char, 0) + 1

        for key in alpha_dict.keys():
            if alpha_dict[key] % 2:
                result += alpha_dict[key] - 1
                has_ood_times += 1
            else:
                result += alpha_dict[key]

        if has_ood_times:
            result += 1

        return result

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
    # write your code here
    # hashmap
        if not s:
            return 0

        alpha_hash = set()
        result = 0

        for char in s:
            if char not in alpha_hash:
                alpha_hash.add(char)
            else:
                alpha_hash.remove(char)
                result += 2

        if len(alpha_hash):
            result += 1

        return result
