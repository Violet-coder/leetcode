"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
"""

import collections
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # A tree: E = v - 1
        # for a undirected graph -> tree: (1) connected (2) acyclic
        # start from the root, BFS, if all the node are visited and there is not cycle, this graph is tree

        # E != v - 1 not tree
        numOfEdges = len(edges)
        if numOfEdges != n - 1:
            return False

        # construct adjencency
        adjencency = [[0] * n for _ in range(n)]
        for i in range(numOfEdges):
            u = edges[i][0]
            v = edges[i][1]
            adjencency[u][v] = 1
            adjencency[v][u] = 1

        # visited list
        visited = [0] * n

        # start from node:0
        # should make the node visited before push into the queue, otherwise could push same node more than one time
        visited[0] = 1
        root = 0
        visitedNodes = 1

        # create queue
        queue = collections.deque([root])

        while queue:
            root = queue.popleft()
            for i in range(n):
                if not adjencency[root][i]:
                    continue
                if not visited[i]:
                    visited[i] = 1
                    visitedNodes += 1
                    queue.append(i)

        if visitedNodes == n:
            return True
        else:
            return False