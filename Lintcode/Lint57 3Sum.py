"""
Description
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

Example
Example 1:

Input:

numbers = [2,7,11,15]
Output:

[]
Explanation:

Cannot find triples such that the sum of three numbers is 0.
Example 2:

Input:

numbers = [-1,0,1,2,-1,-4]
Output:

[[-1, 0, 1],[-1, -1, 2]]
Explanation:

[-1, 0, 1] and [-1, -1, 2] are two triples.1, 2]]
"""


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numbers.sort()
        result = []
        n = len(numbers)

        for i in range(n - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.find_TwoSum(numbers, i + 1, -numbers[i], result)

        return result

    def find_TwoSum(self, nums, start_index, target, result):
        left = start_index
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                result.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

"""
class Solution:
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3:
            return []
        
        numbers.sort()
        result  = []
        n = len(numbers)

        for i in range(n - 2):
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue
            self.find_twoSum(numbers, i + 1, -numbers[i], result)
        
        return result

    def find_twoSum(self, numbers, start_index, target, result):
        left = start_index
        right = len(numbers) - 1

        while left < right:
            if left - 1 >= start_index and numbers[left - 1] == numbers[left]:
                left += 1
                continue
            if right + 1 < len(numbers) and numbers[right + 1] == numbers[right]:
                right -= 1
                continue

            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                result.append([-target, numbers[left], numbers[right]])
                left += 1
                right -= 1
"""
