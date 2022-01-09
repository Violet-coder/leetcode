"""
Merge two given sorted ascending integer array A and B into a new sorted integer array.
Example 1:
Input:
A = [1]
B = [1]
Output:
[1,1]
Explanation:
return array merged.
Example 2:
Input:
A = [1,2,3,4]
B = [2,4,5,6]
Output:
[1,2,2,3,4,4,5,6]
"""


class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        temp = []
        indexA = 0
        indexB = 0

        while indexA < len(A) and indexB < len(B):
            if A[indexA] <= B[indexB]:
                temp.append(A[indexA])
                indexA += 1
            else:
                temp.append(B[indexB])
                indexB += 1

        while indexA < len(A):
            temp.append(A[indexA])
            indexA += 1

        while indexB < len(B):
            temp.append(B[indexB])
            indexB += 1

        return temp

