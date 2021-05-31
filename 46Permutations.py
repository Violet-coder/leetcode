"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        permutations = []
        permutation = []

        self.dfs(nums, set(), permutation, permutations)
        return permutations

    # 递归的定义：找到所有permutation的permutations
    def dfs(self, nums, visited, permutation, permutations):
        # 递归的出口：排列长度等于len(num)->找到了全排列
        if len(permutation) == len(nums):
            permutations.append(list(permutation))

        # 递归的拆解：
        # [] -> [1], [2], [3]..
        # [1] -> [1, 2], [1, 3], [1, 4]..
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(nums, visited, permutation, permutations)
            permutation.pop()
            visited.remove(num)
