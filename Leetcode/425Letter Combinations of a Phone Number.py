"""
Description
Given a digit string excluded 0 and 1, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

Example
Example 1:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Explanation:
'2' could be 'a', 'b' or 'c'
'3' could be 'd', 'e' or 'f'
Example 2:

Input: "5"
Output: ["j", "k", "l"]
"""

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here

        if not digits:
            return []

        results = []
        digit_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        self.dfs([], results, 0, digits, digit_dict)
        print(results)
        return results

    def dfs(self, result, results, index, digits, digit_dict):

        if len(result) == len(digits):
            results.append("".join(list(result)))
            return

        for alpha in digit_dict[digits[index]]:
            result.append(alpha)

            self.dfs(result, results, index + 1, digits, digit_dict)
            result.pop()
