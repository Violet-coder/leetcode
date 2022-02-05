"""
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
Find the number of islands.
Example 1:
Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
Example 2:
Input:
[
  [1,1]
]
Output:
1
"""
import collections


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    # 使用BFS，遇到1就从这个点开始进行BFS，BFS的过程就是把从此点开始的可能连接成岛屿的的点变成0，BFS结束后，实际上这个岛屿就全部变成了0，这样在遍历grid上的点的时候就不会再考虑这个点，因为它属于一个我们已经计算过的岛屿
    # 一次BFS就探索了一个岛屿，进行多少次BFS就有多少个岛屿
    # 但是这个方法会改变原矩阵

    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0

        num_of_islands = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                self.bfs([i, j], grid)
                num_of_islands += 1

        return num_of_islands

    def bfs(self, node, grid):
        queue = collections.deque([node])
        while queue:
            [i, j] = queue.popleft()
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                queue.extend([[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]])



