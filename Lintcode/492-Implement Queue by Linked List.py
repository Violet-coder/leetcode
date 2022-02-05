"""
Implement a Queue by linked list. Support the following basic methods:
enqueue(item). Put a new item in the queue.
dequeue(). Move the first item out of the queue, return it.
Example 1:
Input:
enqueue(1)
enqueue(2)
enqueue(3)
dequeue() // return 1
enqueue(4)
dequeue() // return 2
Example 2:
Input:
enqueue(10)
dequeue()// return 10
"""


class MyQueue1:
    """
    @param: item: An integer
    @return: nothing
    """

    def __init__(self):
        self.queue = []
        self.front = 0
        self.back = 0

    def enqueue(self, item):
        # write your code here
        self.queue.append(item)
        self.back += 1

    """
    @return: An integer
    """

    def dequeue(self):
        # write your code here
        if self.front > self.back:
            return
        dequeue_element = self.queue[self.front]
        self.front += 1
        return dequeue_element
