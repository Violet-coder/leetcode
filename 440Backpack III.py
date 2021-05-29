"""
Description
Given n kinds of items, and each kind of item has an infinite number available. The i-th item has size A[i] and value V[i].
Also given a backpack with size m. What is the maximum value you can put into the backpack?
Example 1:

Input: A = [2, 3, 5, 7], V = [1, 5, 2, 4], m = 10
Output: 15
Explanation: Put three item 1 (A[1] = 3, V[1] = 5) into backpack.
Example 2:

Input: A = [1, 2, 3], V = [1, 2, 3], m = 5
Output: 5
Explanation: Strategy is not unique. For example, put five item 0 (A[0] = 1, V[0] = 1) into backpack.
"""


class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """

    def backPackIII(self, A, V, m):
        # write your code here
        if not A or not V or len(A) != len(V):
            return 0

        n = len(A)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for j in range(m + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - A[i - 1]] + V[i - 1])
                    # count = j//A[i - 1]
                    # for k in range(count + 1):
                    #     dp[i][j] = max(dp[i - 1][j], dp[i][j - count * (A[i - 1])] + count * V[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


