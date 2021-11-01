"""
Description
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
Example 1:
Input:
A = [2,3,1,1,4]
Output:
true
Explanation:
0 -> 1 -> 4 (the number here is subscript) is a reasonable scheme.
Example 2:
Input:
A = [3,2,1,0,4]
Output:
false
Explanation:
There is no solution that can reach the end.
"""


class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        if not A:
            return False

        n = len(A)
        # state: dp[i] represents the possibility to jump to i
        dp = [False] * n

        # initialization: start from 0 and it must be true
        dp[0] = True

        # function
        for i in range(1, n):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break

        # answer
        return dp[n - 1]


