"""
Description
There are n items and a backpack with size m. Given array A representing the size of each item and array V representing the value of each item.
What's the maximum value can you put into the backpack?
Example 1:
Input:
m = 10
A = [2, 3, 5, 7]
V = [1, 5, 2, 4]
Output:
9
Explanation:
Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9
Example 2:
Input:
m = 10
A = [2, 3, 8]
V = [2, 5, 8]
Output:
10
Explanation:
Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10
"""


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        if not A or not V:
            return 0

        n = len(A)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[0][i] = 0

        for i in range(1, n + 1):
            for j in range(m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + V[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


