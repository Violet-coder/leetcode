"""
Description
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return -1 if knight can not reached.
Clarification
If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
Example
Example 1:
Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
"""


class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """

    def shortestPath2(self, grid):
        # write your code here
        distance = 0

        queue = collections.deque([[0, 0]])
        n = len(grid)
        m = len(grid[0])

        while queue:
            distance += 1

            for _ in range(len(queue)):
                point = queue.popleft()
                if point[0] == n - 1 and point[1] == m - 1:
                    return distance - 1
                i = point[0]
                j = point[1]
                if 0 <= i + 1 < len(grid) and 0 <= j + 2 < len(grid[0]) and grid[i + 1][j + 2] == 0:
                    grid[i + 1][j + 2] = 1
                    queue.append([i + 1, j + 2])
                # if 0<= i+1<len(grid) and 0 <=j-2 < len(grid[0]) and grid[i+1][j-2] == 0:
                #     grid[i+1][j-2] = 1
                #     queue.append([i+1, j-2])
                if 0 <= i - 1 < len(grid) and 0 <= j + 2 < len(grid[0]) and grid[i - 1][j + 2] == 0:
                    grid[i - 1][j + 2] = 1
                    queue.append([i - 1, j + 2])
                # if 0<= i-1<len(grid) and 0 <=j-2 < len(grid[0]) and grid[i-1][j-2] == 0:
                #     grid[i-1][j-2] = 1
                #     queue.append([i-1, j-2])
                if 0 <= i + 2 < len(grid) and 0 <= j + 1 < len(grid[0]) and grid[i + 2][j + 1] == 0:
                    grid[i + 2][j + 1] = 1
                    queue.append([i + 2, j + 1])
                # if 0<= i+2<len(grid) and 0 <=j-1 < len(grid[0]) and grid[i+2][j-1] == 0:
                #     grid[i+2][j-1] = 1
                #     queue.append([i+2, j-1])
                if 0 <= i - 2 < len(grid) and 0 <= j + 1 < len(grid[0]) and grid[i - 2][j + 1] == 0:
                    grid[i - 2][j + 1] = 1
                    queue.append([i - 2, j + 1])
                # if 0<= i-2<len(grid) and 0 <=j-1 < len(grid[0]) and grid[i-2][j-1] == 0:
                #     grid[i-2][j-1] = 1
                #     queue.append([i-2, j-1])

        return -1