"""
On a 2 dimensional grid with rows rows and cols columns, we start at (rStart, cStart) facing east.
Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.
Now, we walk in a clockwise spiral shape to visit every position in this grid.
Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.)
Eventually, we reach all rows * cols spaces of the grid.
Return a list of coordinates representing the positions of the grid in the order they were visited.
Example 1:
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
"""


class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """

        total = rows * cols
        row = rStart
        column = cStart
        direction_index = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # boundaries in 4 directions
        path = []
        left, right, top, bottom = cStart - 1, cStart + 1, rStart - 1, rStart + 1

        while len(path) < total:
            if 0 <= row < rows and 0 <= column < cols:
                path.append([row, column])

            if directions[direction_index][1] == 1 and column == right:  # go right and on the right boundary
                direction_index = (direction_index + 1) % 4  # change the direction
                right += 1  # move right boundary to right
            elif directions[direction_index][0] == 1 and row == bottom:  # go down and on the bottom boundary
                direction_index = (direction_index + 1) % 4  # change the direction
                bottom += 1  # move bottom boundary to bottom
            elif directions[direction_index][1] == -1 and column == left:
                direction_index = (direction_index + 1) % 4  # change the direction
                left -= 1  # move left boundary to left
            elif directions[direction_index][0] == -1 and row == top:
                direction_index = (direction_index + 1) % 4  # change the direction
                top -= 1  # move top boundary to top

            row += directions[direction_index][0]
            column += directions[direction_index][1]

        return path
