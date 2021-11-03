"""
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = [0] * n

        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                answer[i - 1] = "FizzBuzz"
            elif not i % 3:
                answer[i - 1] = "Fizz"
            elif not i % 5:
                answer[i - 1] = "Buzz"
            else:
                answer[i - 1] = str(i)

        return answer


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = [0] * n

        for i in range(1, n + 1):
            if not i % 15:
                answer[i - 1] = "FizzBuzz"
            elif not i % 3:
                answer[i - 1] = "Fizz"
            elif not i % 5:
                answer[i - 1] = "Buzz"
            else:
                answer[i - 1] = str(i)

        return answer