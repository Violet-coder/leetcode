# Description
# Given an directed graph, a topological order of the graph nodes is defined as follow:
#
# For each directed edge A -> B in graph, A must before B in the order list.
# The first node in the order can be any node in the graph with no nodes direct to it.
# Find any topological order for the given graph.


#BFS
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

import collections
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        # write your code here
        node_map = {}
        result = []
        # construct the indegree dict node_map
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = 1
                else:
                    node_map[neighbor] += 1

        # the start of the toplogical sort should be the node with 0 indegree
        # put all the nodes with 0 indegree into the queue
        queue = collections.deque([])
        for node in graph:
            if node not in node_map:
                queue.append(node)

        while queue:
            # 每次从队列中拿出一个点放到拓扑序列里，并将该点指向的所有点的入度减1
            # put the first of th queue in to toplocigal sequece, also -1 for all the neighbours
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                node_map[neighbor] -= 1
                # if a node's indegree become 0, put it into queue
                if node_map[neighbor] == 0:
                    queue.append(neighbor)

        return result