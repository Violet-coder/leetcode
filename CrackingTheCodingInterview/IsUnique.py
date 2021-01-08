"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
示例 1：
输入: s = "leetcode"
输出: false
示例 2：
输入: s = "abc"
输出: true
限制：
0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。
"""


class Solution(object):
    # 运用字典键值的唯一性
    def isUnique_dict(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        dic = {char: 1 for char in astr}
        if len(dic) < len(astr):
            return False
        else:
            return True
    #运用散列表
    def isUnique_hashtable(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        alphabet = [None] * 26
        M = 26
        hashcode = 0
        sum = 0
        for char in astr:
            hashcode = (31 * hashcode + ord(char)) % M
            if alphabet[hashcode]:
                sum += 1
                return False
            else:
                alphabet[hashcode] = 1
                hashcode = 0

        return not sum

    #不借助额外的数据结构
    def isUnique_withoutExtraSpace(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        n = len(astr)
        for i in range(n):
            for j in range(i+1, n):
                if astr[i] == astr[j]:
                    return False
        return True
