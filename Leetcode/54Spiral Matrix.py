"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        rows, columns = len(matrix), len(matrix[0])
        visited_matrix = [[False] * columns for _ in range(rows)]
        total = rows * columns
        path = [0] * total

        row = 0
        column = 0
        direction_index = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(total):
            path[i] = matrix[row][column]
            visited_matrix[row][column] = True
            next_row, next_column = row + directions[direction_index][0], column + directions[direction_index][1]

            if not (0 <= next_row < rows and 0 <= next_column < columns and not visited_matrix[next_row][next_column]):
                direction_index = (direction_index + 1) % 4

            row += directions[direction_index][0]
            column += directions[direction_index][1]

        return path


