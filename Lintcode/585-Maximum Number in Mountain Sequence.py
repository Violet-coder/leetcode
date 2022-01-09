"""
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top(Maximum).
Arrays are strictly incremented, strictly decreasing
Example 1:
Input: nums = [1, 2, 4, 8, 6, 3]
Output: 8
Example 2:
Input: nums = [10, 9, 8, 7],
Output: 10
"""


class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return

        n = len(nums)
        start, end = 0, n - 1

        if n == 1:
            return nums[0]

        while start + 1 < end:
            mid = (start + end) // 2  # mid属于偏左的情况,所以mid + 1不会越界
            if nums[mid] < nums[mid + 1]:  # mid处于增区间
                start = mid
            elif nums[mid] > nums[mid + 1]:  # mid处于减区间或者峰值
                end = mid

        return max(nums[start], nums[end])
