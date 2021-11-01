"""
Description
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example 1:

Input: nums = [1,1,2,45,46,46], target = 47
Output: 2
Explanation:

1 + 46 = 47
2 + 45 = 47
"""


class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        numOfPairs = 0

        left, right = 0, len(nums) - 1
        while left < right:
            if left - 1 >= 0 and nums[left] == nums[left - 1]:
                left += 1
                continue
            if right + 1 < len(nums) and nums[right] == nums[right + 1]:
                right -= 1
                continue
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                numOfPairs += 1
                left += 1
                right -= 1

        return numOfPairs




