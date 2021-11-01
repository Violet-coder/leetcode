"""
Description
Given a set of candidate numbers candidates and a target number target. Find all unique combinations in candidates where the numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

1.All numbers (including target) will be positive integers.
2.Numbers in a combination a1, a2, … , ak must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak)
3.Different combinations can be in any order.
4.The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
Example 2:
Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
"""


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
            return []

        n = len(candidates)
        combinations = []
        visited = {}

        self.dfs(candidates, target, visited, [], combinations)

        return combinations

    def dfs(self, candidates, target, visited, combination, combinations):
        combination_key = self.hashKey(sorted(combination))
        if combination_key in visited:
            return

        if self.combination_sum(combination) == target:
            combinations.append(list(sorted(combination)))
            visited[combination_key] = True
            return

        if self.combination_sum(combination) > target:
            return

        for num in candidates:
            combination.append(num)
            self.dfs(candidates, target, visited, combination, combinations)
            combination.pop()

    def combination_sum(self, combination):
        combination_sum = 0
        for num in combination:
            combination_sum += num

        return combination_sum

    def hashKey(self, combination):
        return "".join([str(num) for num in combination])
