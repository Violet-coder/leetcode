import collections
class Solution(object):
    def twoSum_hashset1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Hashset could make it quick to find if the element is in the set, using hashset we could reduce the time complexity of finding target - x in the set from O(N) -> O(1)
        For each of the x, first we check if target - x is already in the set, and then we add x to the set, avoiding we use x twice to treat as a pair incorrectly. E.g.: [2, 4, 5], target = 8
        """
        hashset = set()

        n = len(nums)
        for i in range(n):
            if target - nums[i] in hashset:
                return [nums.index(target - nums[i]), i]
            hashset.add(nums[i])

        return [-1, -1]

    def twoSum_hashset2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        hash_set = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_set:
                return [hash_set[target - nums[i]], i]
            hash_set[nums[i]] = i

        return [-1, -1]

    def twoSum_twopointers(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        tuple_nums = [(number, index) for index, number in enumerate(nums)]
        tuple_nums.sort()

        left, right = 0, len(tuple_nums) - 1

        while left < right:
            if tuple_nums[left][0] + tuple_nums[right][0] > target:
                right -= 1
            elif tuple_nums[left][0] + tuple_nums[right][0] < target:
                left += 1
            else:
                return tuple_nums[left][1], tuple_nums[right][1]

        return [-1, -1]

"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
>>>seq = ['one', 'two', 'three']
>>> for i, element in enumerate(seq):
...     print i, element
... 
0 one
1 two
2 three
"""



