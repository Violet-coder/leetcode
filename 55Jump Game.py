"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
"""
我们利用贪心思想，实时维护最远可达的位置rightmost
依次遍历每个位置i
如果i在rightmost范围内，说明i可达，我们将rightmost更新为max(rightmost, i + A[i])
如果rightmost大于等于数组中的最后一个位置，那就说明最后一个位置可达，我们就可以直接返回True。
如果在遍历结束后，最后一个位置仍然不可达，我们就返回 False 。
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        n = len(nums)

        right_most = 0

        for i in range(n):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
                if right_most >= n - 1:
                    return True

        return False
