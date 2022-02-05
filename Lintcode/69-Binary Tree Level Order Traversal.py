"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
Example 1:
Input:
tree = {1,2,3}
Output:
[[1],[2,3]]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Example 2:

Input:

tree = {1,#,2,3}
Output:

[[1],[2],[3]]
Explanation:

1
 \
  2
 /
3
it will be serialized {1,#,2,3}
"""
import collections

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    # 单队列的实现方式

    def levelOrder(self, root):
        # write your code here
        if not root:
            return []

        queue = collections.deque([root])
        result = []

        while queue:
            result.append([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution1:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    # 双队列的实现方式

    def levelOrder(self, root):
        # write your code here
        if not root:
            return []

        results = []

        queue = [root]
        results = []

        while queue:
            next_queue = []
            results.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue

        return results


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    # Dummy Node的实现方式
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []

        queue = collections.deque([root, None])
        results = []
        level = []

        while queue:
            node = queue.popleft()
            if node is None:
                results.append(level)
                if queue:
                    queue.append(None)
                    level = []
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return results













