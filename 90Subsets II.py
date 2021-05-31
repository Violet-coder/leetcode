"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # hash all the subsets, use hashset as key in the dic visited, every time you want to put subset into subsets, you have to check if this subset is visited(you have alreay put), if key not in the dict, this is a new subset, you could put it in the collection subsets
        subsets = []
        visited = {}
        nums.sort()
        if not nums:
            return subsets

        self.dfs(nums, 0, [], subsets, visited)

        return subsets

    # use this function to generate the key in the dict
    def hashKey(self, subset):
        return '-'.join([str(num) for num in subset])

    def dfs(self, nums, startIndex, subset, subsets, visited):
        subset_key_name = self.hashKey(subset)
        if subset_key_name in visited:
            return

        visited[subset_key_name] = True
        subsets.append(list(subset))

        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets, visited)
            subset.pop()



