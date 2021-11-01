"""
Description
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
The range of input and output data is in int.
Example
Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5
The sum of whole tree is minimum, so return the root.

Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        min_subtree_node, _, _ = self.divideConquer(root)
        return min_subtree_node

    def divideConquer(self, root):
        if not root:
            return root, float("inf"), 0,

        left_min_subtree_node, left_min, left_sum = self.divideConquer(root.left)
        right_min_subtree_node, right_min, right_sum = self.divideConquer(root.right)
        root_sum = left_sum + right_sum + root.val

        if left_min == min(left_min, right_min, root_sum):
            return left_min_subtree_node, left_min, root_sum
        if right_min == min(left_min, right_min, root_sum):
            return right_min_subtree_node, right_min, root_sum
        return root, root_sum, root_sum
