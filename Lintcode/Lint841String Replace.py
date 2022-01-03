"""
Given two identical-sized string array A, B and a string S. All substrings A appearing in S are replaced by B.(Notice: From left to right, it must be replaced if it can be replaced. If there are multiple alternatives, replace longer priorities. After the replacement of the characters can't be replaced again.)

The size of each string array does not exceed 100, the total string length does not exceed 50000.
The lengths of A [i] and B [i] are equal.
The length of S does not exceed 50000.
All characters are lowercase letters.
We guarantee that the A array does not have the same string
Example 1
Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "ababa"

Output: "cccba"
Explanation: In accordance with the rules, the substring that can be replaced is "ab" or "aba". Since "aba" is longer, we replace "aba" with "ccc".
Example 2

Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "aaaaa"

Output: "aaaaa"
Explanation: S does not contain strings in A, so no replacement is done.
Example 3

Input:
A = ["cd","dab","ab"]
B = ["cc","aaa","dd"]
S = "cdab"

Output: "ccdd"
Explanation: From left to right, you can find the "cd" can be replaced at first, so after the replacement becomes "ccab", then you can find "ab" can be replaced, so the string after the replacement is "ccdd".
"""


class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """

    def stringReplace(self, a, b, s):
        # Write your code here
        # hash基底
        seed = 31
        # hash模数
        mod = 1000000007
        # a数组的每个字符串hash值
        aHash = []
        # s字符串的前缀hash值
        sHash = []
        base = []
        for i in a:
            tmp = 0
            # 计算a数组中每个字符串的hash值
            for j in i:
                tmp = tmp * seed + (ord(j) - ord('a'))
                tmp = tmp % mod
            aHash.append(tmp)
        # print(aHash)
        sTmp = 0
        baseTmp = 1
        base.append(baseTmp)
        sHash.append(sTmp)
        for i in s:
            # 计算s字符串的hash值
            sTmp = sTmp * seed + (ord(i) - ord('a'))
            sTmp = sTmp % mod
            sHash.append(sTmp)
            baseTmp = (baseTmp * seed) % mod
            base.append(baseTmp)
        ans = ""
        i = 0
        slen = len(s)
        while i < slen:
            mx = 0
            idx = -1
            # 遍历a数组，找一个和s串匹配的，而且最长的
            for j in range(len(a)):
                aLen = len(a[j])
                if aLen + i > slen:
                    continue
                A = aHash[j]
                S = (sHash[i + aLen] - base[aLen] * sHash[i]) % mod  # 计算s子串的hash值
                A = A % mod
                S = (S + mod) % mod
                if A == S and mx < aLen:
                    mx = aLen
                    idx = j
            if (idx == -1):
                # 没有找到匹配成功的，保留s原串的字母
                ans = ans + s[i:i + 1]
                i = i + 1
            else:
                # 找到匹配的，用b数组对应的字符串替换
                ans = ans + b[idx]
                i = i + mx
        return ans
