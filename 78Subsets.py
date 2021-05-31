"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

#Version-1
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsets = []
        subset = []

        if not nums:
            return subsets

        nums.sort()

        self.dfs(nums, 0, subset, subsets)

        return subsets

    def dfs(self, nums, index, subset, subsets):
        if index == len(nums):
            # need to make a deep copy of the subset otherwise all the subsets will be []
            subsets.append(list(subset))
            return

            # add nums[index]
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, subsets)

        # not add nums[index]
        subset.pop()
        self.dfs(nums, index + 1, subset, subsets)


#Version-2





