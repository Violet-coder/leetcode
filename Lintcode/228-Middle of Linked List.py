"""
Find the middle node of a linked list and return it.
Example 1:
Input:  1->2->3
Output: 2
Explanation: return the middle node.
Example 2:
Input:  1->2
Output: 1
Explanation: If the length of list is even return the center left one.
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if not head:
            return None

        # slow和fast不能同时指向head, 不然会出现快fast如果落在了null，slow会比真正的middle多跳一个node
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow