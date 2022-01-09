"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
Example 1:

Input:

A = [1,2,3]
m = 3
B = [4,5]
n = 2
Output:

[1,2,3,4,5]
Explanation:

After merge, A will be filled as [1,2,3,4,5]
Example 2:

Input:

A = [1,2,5]
m = 3
B = [3,4]
n = 2
Output:

[1,2,3,4,5]
Explanation:

After merge, A will be filled as [1,2,3,4,5]
"""


class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        if not B:
            return

        index = m + n - 1
        indexA = m - 1
        indexB = n - 1

        while indexA >= 0 and indexB >= 0:
            if A[indexA] > B[indexB]:
                A[index] = A[indexA]
                indexA -= 1
            else:
                A[index] = B[indexB]
                indexB -= 1
            index -= 1

        while indexB >= 0:
            A[index] = B[indexB]
            indexB -= 1
            index -= 1



