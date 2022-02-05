class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZerosToCenter(self, nums):
        # write your code here
        if not nums:
            return []

        n = len(nums)
        zero_counter = 0

        # Count the number of zeroes
        for num in nums:
            if num == 0:
                zero_counter += 1

        start = (len(nums) - zero_counter) // 2
        end = start + zero_counter - 1

        # Move some non-zero values to the left of the array
        j = 0
        for i in range(start):
            # Find next non zero value
            while not nums[j] and j < n:
                j += 1
            # Move it to left
            if j < n:
                nums[i] = nums[j]
            j += 1

        # Move other non-zero values to the right of the array
        j = n - 1
        for i in range(n - 1, end, -1):

            while not nums[j] and j >= 0:
                j -= 1
            if j >= 0:
                nums[i] = nums[j]
            j -= 1

        # Fill the middle section with zeroes
        for i in range(start, end + 1):
            nums[i] = 0

        return nums

    def binary(self, number, requests):
        result = []
        for request in requests:
            if request == "+":
                number = self.increment(number)
            else:
                result.append(self.countOne(number))

        return result

    def increment(self, number):
        n = int(number, 2)
        n += 1
        return bin(number)

    def countOne(self, n):

        count = 0
        while n:
            count += 1
            n = (n - 1) & n
        return count




solution = Solution()
outcome = solution.binary("1101", ["?"])
print(outcome)



