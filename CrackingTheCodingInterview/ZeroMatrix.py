"""
编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
示例 1：

输入：
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出：
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2：

输入：
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出：
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""


# 思路：
# 第一次遍历矩阵， 找出矩阵中0出现的位置，用row和column数组记录含有0的列和行
# 第二次遍历矩阵，如果某个元素所在的行或列含有0， 将此元素置0


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix) * [0]
        column = len(matrix[0]) * [0]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == 1 or column[j] == 1:
                    matrix[i][j] = 0
