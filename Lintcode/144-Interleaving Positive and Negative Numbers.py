"""
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.
Example 1
Input : [-1, -2, -3, 4, 5, 6]
Outout : [-1, 5, -2, 4, -3, 6]
Explanation :  any other reasonable answer.
Do it in-place and without extra memory.
"""


class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    # 先把正负数 partition 开，然后再相向双指针进行交换。
    def rerange(self, A):
        # write your code here
        pos = 0
        neg = 0
        # 计算正数和负数的个数
        for num in A:
            if num > 0:
                pos += 1
            else:
                neg += 1
        # 个数多的类型放在前面
        self.partition(A, pos > neg)
        # 交错正负数
        self.interleave(A, pos == neg)

    def partition(self, A, start_pos):
        if start_pos:
            flag = 1
        else:
            flag = -1

        left, right = 0, len(A) - 1

        while left <= right:
            while left <= right and A[left] * flag > 0:
                left += 1
            while left <= right and A[right] * flag < 0:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]

    def interleave(self, A, has_same_length):
        left, right = 1, len(A) - 1

        if has_same_length:
            right = len(A) - 2

        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 2
            right -= 2






