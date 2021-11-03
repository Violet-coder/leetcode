"""
Convert a non-negative integer num to its English words representation.
Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
#Case 1: range(0-999)
class Solution(object):
    def __init__(self):
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                             "Nineteen"]
        self.tens = [" ", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.hundred = []

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        return self.helper(num)

    def helper(self, num):
        if num < 20:
            return self.less_than_20[num]
        elif num < 100:
            return self.tens[num // 10] + " " + self.less_than_20[num % 10]
        else:
            return self.less_than_20[num // 100] + " " + "Hundred" + " " + self.helper(num % 100)

#Case2 range(0-999,999,999):
class Solution(object):
    def __init__(self):
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                             "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                             "Nineteen"]
        self.tens = [" ", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = [" ", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        i = 0
        words = ""
        while num > 0:
            if num % 1000:
                words = self.helper(num % 1000) + self.thousands[i] + " " + words
            num = num // 1000
            i += 1

        return words.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " " + "Hundred" + " " + self.helper(num % 100)