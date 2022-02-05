"""
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.
If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example 1:

Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
Example 2:

Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1
"""


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        # write your code here
        if not grid:
            return -1

        n = len(grid)
        m = len(grid[0])
        source = [0, 0]
        queue = collections.deque([source])
        directions = [(1, 2), (-1, 2), (2, 1), (-2, 1)]
        distance = 0

        while queue:
            distance += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                cur_x = cur[0]
                cur_y = cur[1]
                if cur_x == n - 1 and cur_y == m - 1:
                    return distance - 1
                grid[cur_x][cur_y] = 1
                for direction in directions:
                    next_x = cur_x + direction[0]
                    next_y = cur_y + direction[1]
                    if 0 <= next_x and next_x < n and 0 <= next_y and next_y < m and grid[next_x][next_y] == 0:
                        queue.append([next_x, next_y])
                        grid[next_x][next_y] = 1

        return -1