"""
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:
Input: nums = [4,2,3,4]
Output: 4
"""


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) < 3:
            return 0

        n = len(nums)
        nums.sort()
        result = 0

        for i in range(2, n):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1

        return result