"""
Description
Given n items with size Ai an integer m denotes the size of a backpack. How full you can fill this backpack?
You can not divide any item into small pieces.
Example
Example 1:
Input:
array = [3,4,8,5]
backpack size = 10
Output:9
Explanation:
Load 4 and 5.
Example 2:
Input:
array = [2,3,5,7]
backpack size = 12
Output:12
Explanation:
Load 5 and 7.
"""


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)

        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True

        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - A[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        for i in range(m, -1, -1):
            if dp[n][i]:
                return i
        return -1


