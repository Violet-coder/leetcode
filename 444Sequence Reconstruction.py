"""
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input: org = [1,2,3], seqs = [[1,2],[1,3]]
Output: false
Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
"""


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        indegrees = {}
        adjencency = {}

        # construct the graph
        for seq in seqs:
            if len(seq) == 1:
                if seq[0] not in adjencency:
                    adjencency[seq[0]] = []
                    indegrees[seq[0]] = 0
            else:
                for i in range(len(seq) - 1):
                    if seq[i] not in adjencency:
                        adjencency[seq[i]] = []
                        indegrees[seq[i]] = 0
                    if seq[i + 1] not in adjencency:
                        adjencency[seq[i + 1]] = []
                        indegrees[seq[i + 1]] = 0
                    if seq[i] in adjencency and seq[i + 1] in adjencency:
                        indegrees[seq[i + 1]] += 1
                        adjencency[seq[i]].append(seq[i + 1])

        queue = collections.deque([])
        order = []
        for j in indegrees.keys():
            if not indegrees[j]:
                queue.append(j)

        index = 0
        while queue:
            if len(queue) > 1:
                return False
            cur = queue.popleft()
            if index == len(org) or cur != org[index]:
                return False
            index += 1
            for i in adjencency[cur]:
                indegrees[i] -= 1
                if not indegrees[i]:
                    queue.append(i)

        return index == len(org) and index == len(adjencency)



