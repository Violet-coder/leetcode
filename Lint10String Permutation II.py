"""
Description
Given a string, find all permutations of it without duplicates.
Example 1:
Input:
s = "abb"
Output:
["abb", "bab", "bba"]
Explanation:
There are six kinds of full arrangement of abb, among which there are three kinds after removing duplicates.
Example 2:
Input:
s = "aabb"
Output:
["aabb", "abab", "baba", "bbaa", "abba", "baab"]
"""


class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        # write your code here
        if not str:
            return [""]

        chars = sorted(list(str))
        permutations = []
        n = len(chars)
        visited = [False] * n

        self.dfs(chars, visited, [], permutations)

        return permutations

    def dfs(self, chars, visited, permutation, permutations):
        if len(permutation) == len(chars):
            permutations.append("".join(list(permutation)))
            return

        for i in range(len(chars)):
            if visited[i]:
                continue

            if i > 0 and chars[i - 1] == chars[i] and not visited[i - 1]:
                continue

            permutation.append(chars[i])
            visited[i] = True
            self.dfs(chars, visited, permutation, permutations)
            permutation.pop()
            visited[i] = False


