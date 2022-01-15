"""
Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.
Example 1:
Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
Example 2:
Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
O(logn) time, n is the first index of the given target number.
"""


class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        # write your code here
        n = self.findRightBoundary(reader, target)
        print("boundary", n)
        if reader.get(n) < target:
            return -1

        start, end = 0, n

        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1

    def findRightBoundary(self, reader, target):
        boundary = 1
        while reader.get(boundary) != 2147483647 and reader.get(boundary) < target:
            boundary *= 2

        while reader.get(boundary) == 2147483647:
            boundary -= 1

        return boundary


class Solution1:
    # @param {ArrayReader} reader: An instance of ArrayReader
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        kth = 1
        while reader.get(kth - 1) < target:
            kth = kth * 2

        # start 也可以是 kth // 2，但是我习惯比较保守的写法
        # 因为写为 0 也不会影响时间复杂度
        start, end = 0, kth - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
