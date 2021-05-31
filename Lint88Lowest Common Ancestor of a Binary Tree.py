"""
Description
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Example 1:

Input:

tree = {1}
A = 1
B = 1
Output:

1
Explanation:

For the following binary tree（only one node）:
        1
LCA(1,1) = 1
Example 2:

Input:

tree = {4,3,7,#,#,5,6}
A = 3
B = 5
Output:

4
Explanation:

For the following binary tree:

     4
    / \
   3   7
      / \
     5   6

LCA(3, 5) = 4
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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        node = root

        while node:
            if self.isCommonAncestor(node, A, B):
                if not self.isCommonAncestor(node.left, A, B) and not self.isCommonAncestor(node.right, A, B):
                    return node
                elif self.isCommonAncestor(node.left, A, B):
                    node = node.left
                else:
                    node = node.right
            else:
                break

        return None

    def isCommonAncestor(self, node, targetNode1, targetNode2):
        print(self.isAncestor(node, targetNode1))
        return self.isAncestor(node, targetNode1) and self.isAncestor(node, targetNode2)

    def isAncestor(self, node, targetNode):
        if not node:
            return False

        if node == targetNode or node == targetNode:
            return True

        in_left = self.isAncestor(node.left, targetNode)
        in_right = self.isAncestor(node.right, targetNode)

        return in_left or in_right






