class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target-num] = i

    """
    def twoSum(self, numbers, target):
        hashset = set()
        for number in numbers:
            if target - number in hashset:
                return number, target - number
            hashset.add(number)   
        return [-1, -1]      
    """
    def twoSum_list (self, nums, target):
        i = list()
        for num in nums:
            if target - num in i:
                i.append(num)
                return [i.index(target - num), i.index(num, i.index(target - num)+1)]
            i.append(num)
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
# outcome = solution.twoSum([2, 7, 11, 15], 9)
# outcome = solution.twoSum_list([0,4,3,0], 0)
outcome = solution.twoSum5([2, 7, 11, 15], 24)
print(outcome)
a= {1, 2, 3, 4, 5};
i = 1;
print();
