"""
Give a two-dimensional grid, each grid has a value, 2 for wall, 1 for zombie, 0 for human (numbers 0, 1, 2).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
Example 1:
Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2
"""
import collections
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        # write your code here
        if not grid:
            return 0
        days = 0

        queue = collections.deque([])

        m = len(grid)
        n = len(grid[0])

        people = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])
                if grid[i][j] == 0:
                    people += 1

        while queue:
            days += 1

            for i in range(len(queue)):
                z = queue.popleft()
                z_x, z_y = z[0], z[1]

                if z_x - 1 >= 0 and z_y < n and grid[z_x - 1][z_y] == 0:
                    queue.append([z_x - 1, z_y])
                    grid[z_x - 1][z_y] = 1
                    people -= 1
                if z_x + 1 < m and z_y < n and grid[z_x + 1][z_y] == 0:
                    queue.append([z_x + 1, z_y])
                    grid[z_x + 1][z_y] = 1
                    people -= 1
                if z_x < m and z_y + 1 < n and grid[z_x][z_y + 1] == 0:
                    queue.append([z_x, z_y + 1])
                    grid[z_x][z_y + 1] = 1
                    people -= 1
                if z_x < m and z_y - 1 >= 0 and grid[z_x][z_y - 1] == 0:
                    queue.append([z_x, z_y - 1])
                    grid[z_x][z_y - 1] = 1
                    people -= 1

            if not people:
                return days

        return -1

    def allZombines(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return False
        return True





