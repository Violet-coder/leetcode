"""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
Example 1:
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        node = root
        closest = float("inf")

        while node:
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            if node.val < target:
                node = node.right
            else:
                node = node.left

        return closest
