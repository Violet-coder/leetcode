"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Before taking some courses, you need to take other courses. For example, to learn course 0, you need to learn course 1 first, which is expressed as [0,1].
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Example 1:

Input: n = 2, prerequisites = [[1,0]]
Output: true
Example 2:

Input: n = 2, prerequisites = [[1,0],[0,1]]
Output: false
"""


class Solution:
    """
    @param numCourses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        indegrees = {}
        result = []
        graph = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
            if prerequisite[1] not in indegrees:
                indegrees[prerequisite[1]] = 1
            else:
                indegrees[prerequisite[1]] += 1

        queue = collections.deque([])
        for i in range(numCourses):
            if i not in indegrees:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)
            for next_course in graph[node]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append(next_course)

        return len(result) == numCourses



