"""
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

示例1:

 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
示例2:

 输入：s1 = "aa", s2 = "aba"
 输出：False
提示：

字符串长度在[0, 100000]范围内。
说明:

你能只调用一次检查子串的方法吗？
"""


# 思路：
# 本质上，我们是在寻找是否有一种方式可以把第一个字符串分成两部分，即x和y, 第一个字符串就是xy，第二个字符串就是yx。
# 如果将xy与自身连接，那么yx一定包含在xy中。
# 若两个字符串可以轮转得到，则s2肯定在s1 + s1的子集内
# 字符串旋转就是在某个位置断开字符串,然后把前一段放到后一段的后面,比如"12345",在23之间断开,变成"34512",就是把前一段放在后一段后面;
# 我们自连接s1,得到"1234512345", 那么我们可以发现s1+s1包含所有s1的字符串轮转（1在后面,12在后面,123在后面,1234在后面,12345在后面），所以如果s2是s1的字符串轮转, 那么它一定包含在s1+s1中

class Solution(object):
    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        if s2 in s1 + s1:
            return True
        else:
            return False
