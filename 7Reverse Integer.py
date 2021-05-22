"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = []
        abs_num = abs(x)
        reversed_num = 0

        while abs_num:
            digit = abs_num % 10
            result.append(digit)
            abs_num = abs_num // 10

        n = len(result)

        for i in range(n):
            reversed_num += result[i] * math.pow(10, n - i - 1)
            if int(reversed_num) > 0x7fffffff:
                return 0

        if x >= 0:
            return int(reversed_num)
        else:
            return -int(reversed_num)