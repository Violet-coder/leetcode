"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: n = 2, prerequisites = [[1,0]]
Output: [0,1]
Example 2:

Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
"""


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """

    def findOrder(self, numCourses, prerequisites):
        # write your code here
        indegrees = {}
        graph = [[] for _ in range(numCourses)]
        result = []

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            if prerequisite[0] not in indegrees:
                indegrees[prerequisite[0]] = 1
            else:
                indegrees[prerequisite[0]] += 1

        queue = collections.deque([])
        for i in range(numCourses):
            if i not in indegrees:
                queue.append(i)

        while queue:
            cur_course = queue.popleft()
            result.append(cur_course)
            for next_course in graph[cur_course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append(next_course)

        if len(result) == numCourses:
            return result

        return []

