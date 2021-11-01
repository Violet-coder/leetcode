"""
Description
Find the middle node of a linked list and return it.

Example
Example 1:

Input:  1->2->3
Output: 2
Explanation: return the middle node.
Example 2:

Input:  1->2
Output: 1
Explanation: If the length of list is even return the center left one.
Challenge
If the linked list is a data stream, can you find the middle node without iterating the linked list again?
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

        # get the length of the linked list
        node = head
        linkedListLength = 0
        linkedListArray = []

        while node:
            linkedListArray.append(node)
            linkedListLength += 1
            node = node.next

        if not linkedListLength:
            return None
        if linkedListLength % 2:
            middle = linkedListLength // 2
        else:
            middle = linkedListLength // 2 - 1

        return linkedListArray[middle]



