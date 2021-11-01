"""
Description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.The overall run time complexity should be O(log(m + n))O(log(m+n)).
The definition of the median:
The median here is equivalent to the median in the mathematical definition.
The median is the middle of the sorted array.
If there are n numbers in the array and n is an odd number, the median is A[(n - 1) / 2]A[(n−1)/2].
If there are n numbers in the array and n is even, the median is A[(n - 1) / 2] + A[(n - 1) / 2 + 1]) / 2A[(n−1)/2]+A[(n−1)/2+1])/2.
For example, the median of the array A=[1,2,3] is 2, and the median of the array A=[1,19] is 10.Example 1:
Input:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
Output:
3.5
"""

# merge two sorted array and find the median of two sorted array
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        # first merge two sorted arrays
        i = 0
        j = 0
        merged_array = []

        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                merged_array.append(A[i])
                i += 1
            else:
                merged_array.append(B[j])
                j += 1

        merged_array += A[i:]
        merged_array += B[j:]

        n = len(merged_array)

        if n % 2:
            return merged_array[(n - 1) // 2]
        else:
            return (merged_array[n // 2 - 1] + merged_array[n // 2]) / 2

#

