"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Example 1:
Input:
array = [4, 5, 1, 2, 3]
target = 1
Output:
2
Explanation:
1 is indexed at 2 in the array.
Example 2:
Input:
array = [4, 5, 1, 2, 3]
target = 0
Output:
-1
Explanation:
0 is not in the array. Returns -1.
O(logN) time
"""


class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        n = len(A)
        if n == 1:
            if A[0] == target:
                return 0
            else:
                return -1
        targetIndex = -1
        pivot = self.findPivot(A)
        if target >= A[0]:
            targetIndex = self.binarySearch(0, pivot, A, target)
        else:
            if pivot + 1 > n - 1:
                return -1
            targetIndex = self.binarySearch(pivot + 1, n - 1, A, target)

        return targetIndex

    def findPivot(self, nums):
        n = len(nums)
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[0]:
                end = mid
            else:
                start = mid
        if nums[start] > nums[end]:
            return start
        else:
            return end

    def binarySearch(self, start, end, nums, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


class Solution1:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        # write your code here
        if not A:
            return -1

        n = len(A)
        start, end = 0, n - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[start] < A[mid]:
                if A[start] <= target and A[mid] > target:
                    end = mid
                else:
                    start = mid
            else:
                if A[start] > target and A[mid] < target:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1
