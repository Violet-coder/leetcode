"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # first reverse up to down, then swap the symmetry
        # 1 2 3     7 8 9     7 4 1
        # 4 5 6  => 4 5 6  => 8 5 2
        # 7 8 9     1 2 3     9 6 3
        n = len(matrix)
        matrix.reverse()
        temp = None

        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp




