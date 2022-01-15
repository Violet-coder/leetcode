"""
Given target, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
Example 1:
Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
Example 2:
Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
"""


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A:
            return []

        n = len(A)
        nearset_num_index = self.find_nearest(A, target)

        left = nearset_num_index
        right = nearset_num_index + 1
        result = []
        while left >= 0 and right < n:
            if len(result) == k:
                break
            if abs(A[left] - target) <= abs(A[right] - target):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1

        if len(result) == k:
            return result

        if left < 0:
            result.extend(A[right: right + k - len(result)])
        else:
            for i in range(left, left - (k - len(result)), -1):
                result.append(A[i])

        return result

    def find_nearest(self, nums, target):
        n = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return n - 1
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            mid_next = mid + 1
            mid_distance = abs(nums[mid] - target)
            mid_next_distance = abs(nums[mid_next] - target)
            if mid_distance < mid_next_distance:
                end = mid
            else:
                start = mid

        if abs(nums[start] - target) <= abs(nums[end] - target):
            return start
        else:
            return end




