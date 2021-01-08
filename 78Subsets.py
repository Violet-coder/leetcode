class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        results = []
        if nums is None:
            return results
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums, index, subset, results):
        results.append(list(subset))

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, results)
            subset.pop()


solution = Solution()
outcome = solution.subsets([1, 2, 3])
print(outcome)


