"""
Description
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Example 1:

Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def __init__(self):
        self.kth = 0
        self.smallest = float("inf")

    def kthSmallest(self, root, k):
        # write your code here
        # BST: norder tranverse
        self.kth = k
        self.dfs(root)
        return self.smallest

    def dfs(self, root):
        if not root:
            return None
        self.dfs(root.left)

        self.kth -= 1
        if self.kth == 0:
            self.smallest = root.val

        self.dfs(root.right)


