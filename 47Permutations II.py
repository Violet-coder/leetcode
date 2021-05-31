"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        nums.sort()
        permutations = []

        n = len(nums)
        visited = [False] * n

        self.dfs(nums, visited, [], permutations)

        return permutations

    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                continue

            permutation.append(nums[i])
            visited[i] = True
            self.dfs(nums, visited, permutation, permutations)
            permutation.pop()
            visited[i] = False


