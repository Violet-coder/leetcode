"""
There is an integer array which has the following features:
The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:
A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.
It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
Example 1:

Input:

A = [1, 2, 1, 3, 4, 5, 7, 6]
Output:
1
Explanation:
Returns the index of any peak element. 6 is also correct.
Example 2:
Input:
A = [1,2,3,4,1]
Output:
3
Explanation:
return the index of peek.
"""


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        # write your code here
        n = len(A)
        start, end = 0, n - 1

        while start + 1 < end:
            mid = (start + end) // 2
            mid_right = mid + 1
            if A[mid] < A[mid_right]:
                start = mid
            else:
                end = mid

        if A[start] > A[end]:
            return start
        else:
            return end
