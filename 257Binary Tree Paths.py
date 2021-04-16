"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        paths = []
        if root:
            path.append(root)
            self.findPaths(root, path, paths)
            return paths
        else:
            return []

    def findPaths(self, node, path, paths):
        if not node:
            return
        if not node.left and not node.right:
            paths.append("->".join([str(node.val) for node in path]))

        path.append(node.left)
        self.findPaths(node.left, path, paths)
        path.pop()
        path.append(node.right)
        self.findPaths(node.right, path, paths)
        path.pop()

