"""
Design and implement a TwoSum class. It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
Example 1:
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""

# 用双指针的方法:add操作是O(1), find操作是O(nlogn)
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    nums = []

    def add(self, number):
        # write your code here
        self.nums.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        if not self.nums:
            return False

        n = len(self.nums)
        self.nums.sort()
        left, right = 0, n - 1

        while left < right:
            if self.nums[left] + self.nums[right] == value:
                return True
            elif self.nums[left] + self.nums[right] < value:
                left += 1
            else:
                right -= 1

        return False


# 用哈希表的方法:add操作是O(1), find操作是O(n)
class TwoSum1:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.counter = {}

    def add(self, number):
        # write your code here
        self.counter[number] = self.counter.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for num1 in self.counter:
            num2 = value - num1
            if num1 == num2 and self.counter[num1] >= 2:
                return True
            if num1 != num2 and num2 in self.counter:
                return True
        return False



