"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm withO(log n) runtime complexity.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 看到排序和搜索的关键字应该要能都想到二分搜索， 有序或部分有序， 基本使用二分法及其变种
        # 二分搜索在于要能够丢弃一半的数据
        # 此题与经典的二分搜索的区别在于每次二分的时候一边的数据是有序的一边是无序的
        # 变化在与如何丢弃数据
        if not nums:
            return -1

        n = len(nums)
        start, end = 0, n - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= nums[0]:  # mid在左半段
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target and target >= nums[0]:
                    end = mid
                else:
                    start = mid
            else:  # mid在右半段
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target and target <= nums[n - 1]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1