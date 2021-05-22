class Solution(object):
    def twoSum_hashset(self, nums, target):
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
    描述给定一个整数数组，找出这个数组中有多少对的和是小于或等于目标值。返回对数。
    Enter: nums = [2, 7, 11, 15], target = 24. 输出: 5. 
    Explanation:
    2 + 7 < 24
    2 + 11 < 24
    2 + 15 < 24
    7 + 11 < 24
    7 + 15 < 24
    """
    def twoSum5(self, nums, target):
        nums.sort()
        left, right = 0, len(nums)-1
        pair_num = 0

        while left < right:
            if nums[left] + nums[right] <= target:
                pair_num += right - left
                left += 1
            else:
                right -= 1
        return pair_num


solution = Solution()
outcome = solution.twoSum5([2, 7, 11, 15], 24)
print(outcome)

