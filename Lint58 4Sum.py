"""
Description
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

Example
Example 1:

Input:

numbers = [2,7,11,15]
target = 3
Output:

[]
Explanation:

2 + 7 + 11 + 15 != 3. There is no quadruple satisfying the condition.
Example 2:

Input:

numbers = [1,0,-1,0,-2,2]
target = 0
Output:

[[-1, 0, 0, 1],[-2, -1, 1, 2],[-2, 0, 0, 2]]
Explanation:

There are three different quadruples whose sum of four numbers is 0.
"""


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        # write your code here
        if not numbers or len(numbers) < 4:
            return []

        numbers.sort()
        result = []
        n = len(numbers)

        for i in range(n - 4):
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue
            for j in range(i + 1, n - 3):
                if j > i + 1 and numbers[j - 1] == numbers[j]:
                    continue
                self.find_TwoSum(numbers, j + 1, target - numbers[i] - numbers[j], result, numbers[i], numbers[j])

        return result

    def find_TwoSum(self, numbers, start_index, target, result, a, b):
        left = start_index
        right = len(numbers) - 1

        while left < right:
            if left - 1 >= start_index and numbers[left - 1] == numbers[left]:
                left += 1
                continue
            if right + 1 < len(numbers) and numbers[right] == numbers[right + 1]:
                right -= 1
                continue

            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                result.append([a, b, numbers[left], numbers[right]])
                left += 1
                right -= 1









