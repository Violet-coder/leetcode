"""
For a given source string and a target string, you should output the first index(from 0) of target string in the source string.If the target does not exist in source, just return -1.
Example 1:
Input:
source = "source"
target = "target"
Output:
-1
Explanation:
If the source does not contain the target's content, return - 1.

Example 2:
Input:
source = "abcdabcdefg"
target = "bcd"
Output:
1
Explanation:
If the source contains the target's content, return the location where the target first appeared in the source.
"""


class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        if not target:
            return 0

        n = len(source)

        for i in range(n - len(target) + 1):
            not_equal = False
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    not_equal = True
                    break
            if not not_equal:
                return i

        return -1



