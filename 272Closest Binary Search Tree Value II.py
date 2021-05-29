"""
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example 1:
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:
Input: root = [1], target = 0.000000, k = 1
Output: [1]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if root is None or k == 0:
            return []

        # get the inored of the BST which will be a sorted array
        nums = self.get_inorder(root)
        # use binary search to find the closet position which is smaller than the target
        left = self.find_lower_index(nums, target)
        right = left + 1
        results = []

        # Use two pointers to move to two sides
        for _ in range(k):
            if self.is_left_closer(nums, left, right, target):
                results.append(nums[left])
                left -= 1
            else:
                results.append(nums[right])
                right += 1

        return results

    def get_inorder(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []

        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)

        return inorder

    def find_lower_index(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] < target:
            return end
        if nums[start] < target:
            return start

        return -1

    def is_left_closer(self, nums, left, right, target):
        if left < 0:
            return False
        if right >= len(nums):
            return True
        return target - nums[left] < nums[right] - target











