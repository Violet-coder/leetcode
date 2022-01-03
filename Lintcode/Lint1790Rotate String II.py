"""
Description
Given a string(Given in the way of char array), a right offset and a left offset, move the string according to the given offset and save it in a new result set. (left offest represents the offset of a string to the left,right offest represents the offset of a string to the right,the total offset is calculated from the left offset and the right offset, split two strings at the total offset and swap positions)
Example 1:

Input：str ="abcdefg", left = 3, right = 1
Output："cdefgab"
Explanation：The left offset is 3, the right offset is 1, and the total offset is left 2. Therefore, the original string moves to the left and becomes "cdefg"+ "ab".
Example 2:

Input：str="abcdefg", left = 0, right = 0
Output："abcdefg"
Explanation：The left offset is 0, the right offset is 0, and the total offset is 0. So the string remains unchanged.
Example 3:

Input：str = "abcdefg",left = 1, right = 2
Output："gabcdef"
Explanation：The left offset is 1, the right offset is 2, and the total offset is right 1. Therefore, the original string moves to the left and becomes "g" + "abcdef".
"""


class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """

    def RotateString2(self, str, left, right):
        # write your code here
        offset = (left - right) % len(str)
        rotated_str = ""

        if offset > 0:
            rotated_str = str[offset:] + str[:offset]
            return rotated_str

        if offset < 0:
            rotated_str = str[:abs(offset)] + str[abs(offset):]
            return rotated_str

        return str
"""
余数：在编译器中，两个异号的数取余之后的结果取决于分子的符号。
负数%负数：将分母的负数自动转换为正整数，然后再将分子负数的负号提取出来，将两个正整数取余，最后的结果加上负号就好了。
负数%正数：编译器先将分子负数的负号提取出来，将两个正整数取余，最后结果加上负号即可。
正数%负数：编译器自动将分母负数转换为正整数，然后两个正整数取余得到就是最终结果。
"""
