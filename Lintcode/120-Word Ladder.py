"""
Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, output the length of the sequence.
Transformation rule such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary. (Start and end words do not need to appear in the dictionary )
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the dictionary.
You may assume beginWord and endWord are non-empty and are not the same.
len(dict) <= 5000, len(start) < 5len(dict)<=5000,len(start)<5
Example 1:
Input:
start = "a"
end = "c"
dict =["a","b","c"]
Output:
2
Explanation:
"a"->"c"
Example 2:
Input:
start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]
Output:
5
Explanation:
"hit"->"hot"->"dot"->"dog"->"cog"
"""


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # write your code here
        queue = collections.deque([start])
        distance = 0
        visited = set([start])
        dict_set = set(dict)

        while queue:
            distance += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                if self.one_char_different(cur, end):
                    return distance + 1
                next_level = self.possible_one_char_transitions(cur, dict_set)
                for word in next_level:
                    if word in visited:
                        continue
                    queue.append(word)
                    visited.add(word)

        return distance

    def possible_one_char_transitions(self, targetWord, dict_set):
        candidates = []

        for i in range(len(targetWord)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                targetWord_copy = targetWord
                targetWord_copy = targetWord_copy[:i] + char + targetWord_copy[i + 1:]
                if targetWord_copy in dict_set:
                    candidates.append(targetWord_copy)
        return candidates

    def one_char_different(self, word1, word2):
        difference = 0

        for i in range(len(word1)):
            if word1[i] != word2[i]:
                difference += 1

        if difference == 1:
            return True

        return False
