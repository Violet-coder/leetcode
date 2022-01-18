"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.
Example 1:
Input:
nums = []
k = 9
Output:
0
Explanation:
Empty array, print 0.
Example 2:
Input:
nums = [3,2,2,1]
k = 2
Output:
1
Explanation:
the real array is[1,2,2,3].So return 1.
"""


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0

        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

        return left
