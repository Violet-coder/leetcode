"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:
Input: n = 1
Output: [[1]]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        rows = n
        columns = n
        total = n * n

        matrix = [[0] * n for _ in range(n)]

        row = 0
        column = 0
        direction_index = 0

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(1, total + 1):
            matrix[row][column] = i
            next_row, next_column = row + directions[direction_index][0], column + directions[direction_index][1]
            if not (0 <= next_row < n and 0 <= next_column < n and not matrix[next_row][next_column]):
                direction_index = (direction_index + 1) % 4

            row += directions[direction_index][0]
            column += directions[direction_index][1]

        return matrix








