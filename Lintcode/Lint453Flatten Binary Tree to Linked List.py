"""
Description
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.
Example
Example 1:

Input:{1,2,5,3,4,#,6}
Output：{1,#,2,#,3,#,4,#,5,#,6}
Explanation：
     1
    / \
   2   5
  / \   \
 3   4   6

1
\
 2
  \
   3
    \
     4
      \
       5
        \
         6
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        if not root:
            return

        self.divideConquer(root)

    # 变成假链表的过程，就是将root的right指向左子树，左子树的尾节点指向右子树，最后再将左子树置空。返回尾节点即可。

    def divideConquer(self, root):
        if not root:
            return None

        left_last = self.divideConquer(root.left)  # tail of left linked list
        right_last = self.divideConquer(root.right)  # tail of right linked list

        if left_last:
            left_last.right = root.right
            root.right = root.left

        root.left = None

        if right_last:
            return right_last
        elif left_last:
            return left_last
        else:
            return root
