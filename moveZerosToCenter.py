class Solution(object):
    def moveZerosToCenter(self, arr):
        numZeroes = 0
        # Count how the number of zeroes
        for i in range(len(arr)):
            if arr[i] == 0:
                numZeroes += 1

        # Determine the range of zeores
        first = (len(arr) - numZeroes) // 2
        last = first + numZeroes - 1

        j = 0
        # Move some non-zero values to the left of the array
        for i in range(first):
            # Find next non zero value
            while not arr[j]:
                j += 1
            # Move it to left
            arr[i] = arr[j]
            j += 1

        # Move other non-zero values to the right of the array
        j = len(arr) - 1
        for i in range(len(arr) - 1, last, -1):
            while not arr[j]:
                j -= 1
            arr[i] = arr[j]
            j -= 1

        # Fill the middle section with zeroes
        for i in range(first, last+1):
            arr[i] = 0

        return arr

solution = Solution()
outcome = solution.moveZerosToCenter([0, 1, 3, 5, 0, 7, 8])
print(outcome)

