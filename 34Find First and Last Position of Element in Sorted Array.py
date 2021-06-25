"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 先使用二分查找查找任意一个target所在的位置，再去寻找给定目标值在数组中的开始位置和结束位置。
        if not nums:
            return [-1, -1]

        n = len(nums)

        start = 0
        end = n - 1
        position = -1
        rightEnd = -1

        if target < nums[start] or target > nums[end]:
            return [-1, -1]

        while start + 1 < end:
            mid = (start + end) / 2
            if target == nums[mid]:
                position = mid
                break
            elif target < nums[mid]:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            position = start

        if nums[end] == target:
            position = end

        if position == -1:
            return [-1, -1]

        leftStart = position
        while leftStart >= 0:
            if nums[leftStart] != target:
                break
            leftStart -= 1

        rightEnd = position
        while rightEnd < n:
            if nums[rightEnd] != target:
                break
            rightEnd += 1

        return [leftStart + 1, rightEnd - 1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用两次二分查找分别查找开始位置和结束位置
        if not nums:
            return [-1, -1]

        leftIndex = self.findFirstPosition(nums, target)

        if leftIndex == -1:
            return [-1, -1]

        rightIndex = self.findLastPosition(nums, target)
        return [leftIndex, rightIndex]

    def findFirstPosition(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def findLastPosition(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1


