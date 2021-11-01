"""
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning It is guaranteed that such a partitioning exists.
Example 1:
Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:
Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
"""


class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        n = len(nums)

        maxLeft = [None] * n
        minRight = [None] * n

        maxLeft[0] = nums[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], nums[i])

        minRight[-1] = nums[-1]
        for i in range(n - 1, 0, -1):
            minRight[i - 1] = min(minRight[i], nums[i - 1])

        for i in range(1, n):
            if maxLeft[i - 1] <= minRight[i]:
                return i

        return 0