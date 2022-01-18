"""
Description
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Example
Example 1:

Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
Example 2:

Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
"""


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here

        # partition choose the pivot as 0
        if not nums:
            return

        left, right = 0, 0
        # right指针扫描数组，right指针的位置>=left，遇到最近的不为0的数就交换给left, 然后去找下一个不为0的数
        # 在没有遇到0的时候，right与left是重合的，在right遇到0之后，right会在left右侧
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    """
    使用两个指针right和left，left为新数组的指针，right为原数组的指针，原数组指针向后扫，遇到非0的数就赋值给新数组的指针位置，并将新数组指针向后移动
    1. 将两个指针先指向0，即数组头部
    2. right向后扫描，当遇到非0数即nums[right] != 0时，将其赋值给新数组指针指向的位置，即nums[left] = nums[right]，并将left向后移动一位
    3. 若新数组指针还未指向尾部，即剩余的位置都是0，将剩余数组赋值为0
    """

    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return []

        n = len(nums)

        # 将两个指针先指向数组头部
        left, right = 0, 0

        while right < n:
            # 遇到非0数赋值给新数组指针指向的位置
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1

        # 若新数组指针还未指向尾部，将剩余数组赋值为0
        while left < n:
            nums[left] = 0
            left += 1

        return nums
