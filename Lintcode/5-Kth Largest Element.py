"""
Find the K-th largest element in an array.

You can swap elements in the array.
1 \leq k \leq 10^{5}1≤k≤10
5


样例
Example 1:

Input:

k = 1
nums = [1,3,4,2]
Output:

4
Explanation:

The first largest element is four.

Example 2:

Input:

k = 3
nums = [9,3,2,4,8]
Output:

4
Explanation:

The third largest largest element is four.

挑战
O(n) time, O(1) extra memory.
"""


class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, k, nums):
        # write your code here
        if not nums:
            return -1

        return self.quickSelect(0, len(nums) - 1, k, nums)

    def quickSelect(self, start, end, k, nums):
        if start == end:
            return nums[start]

        left = start
        right = end
        pivot = nums[(left + right) // 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.quickSelect(start, right, k, nums)

        if start + k - 1 >= left:
            return self.quickSelect(left, end, k - (left - start), nums)

        return nums[right + 1]





