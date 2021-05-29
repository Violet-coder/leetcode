"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_balanced, _ = self.divideAndConquer(root)

        return is_balanced

    def divideAndConquer(self, root):
        # return if_balanced and height
        if not root:
            return True, 0

        is_left_balanced, left_height = self.divideAndConquer(root.left)
        is_right_balanced, right_height = self.divideAndConquer(root.right)

        height = max(left_height, right_height) + 1

        if not is_left_balanced or not is_right_balanced:
            return False, height

        if abs(left_height - right_height) > 1:
            return False, height

        return True, height
