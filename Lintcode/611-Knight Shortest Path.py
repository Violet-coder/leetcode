"""
Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, find the shortest path to a destination position, return the length of the route.
Return -1 if destination cannot be reached.
source and destination must be empty.
Knight can not enter the barrier.
Path length refers to the number of steps the knight takes.
If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
Example 1:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
Example 2:

Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
Output:-1
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        if not source:
            return -1

        distance = 0
        queue = collections.deque([source])
        m = len(grid)
        n = len(grid[0])

        direction = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        while queue:
            distance += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.x == destination.x and node.y == destination.y:
                    return distance - 1
                grid[node.x][node.y] = 1
                for delta_x, delta_y in direction:
                    node_x, node_y = node.x + delta_x, node.y + delta_y
                    if 0 <= node_x < m and 0 <= node_y < n and grid[node_x][node_y] == 0:
                        grid[node_x][node_y] = 1
                        queue.append(Point(node_x, node_y))
        return -1