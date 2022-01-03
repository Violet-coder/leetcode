"""
Implement strStr function in O(n + m) time.
strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.
Example 1:

Input：source = "abcdef"， target = "bcd"
Output：1
Explanation：
The position of the first occurrence of a string is 1.
Example 2:

Input：source = "abcde"， target = "e"
Output：4
Explanation：
The position of the first occurrence of a string
"""


class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        m = len(target)
        n = len(source)
        if m == 0:
            return 0

        BASE = pow(10, 6)
        power = 1
        for i in range(m):
            power = power * 31 % BASE

        target_hashcode = 0
        for i in range(m):
            target_hashcode = (target_hashcode * 31 + ord(target[i])) % BASE

        hashcode = 0
        for i in range(n):
            hashcode = (hashcode * 31 + ord(source[i])) % BASE
            if i < m:
                continue
            if i >= m:
                hashcode = hashcode - ord(source[i - m]) * power % BASE
                if hashcode < 0:
                    hashcode += BASE
            if hashcode == target_hashcode:
                if source[i - m + 1: i + 1] == target:
                    return i - m + 1

        return -1

