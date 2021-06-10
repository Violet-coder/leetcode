"""
Write code to convert a given number into words. For example, if “123” is given as input, output should be “one thousand two hundred twenty three”(Range 0 -999).
"""
class Solution(object):
    def __init__(self):
        self.less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen","Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    #Range(0 -999)
    def convert_to_words_1(self, num):
        if num == 0:
            return "Zero"

        return self.helper(num)

    def helper(self, num):
        if num < 20:
            return self.less_than_20[num]
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num%10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(num%100)

    def convert_to_words_2(self, num):
        if num == 0:
            return "Zero"

        i = 0
        words = ""

        while num > 0:
            if num % 1000 != 0:
                words = self.helper(num % 1000) + self.thousands[i] + " " + words
            num = num // 1000
            i += 1

        return words.strip()

    def helper_2(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(num % 100)

# solution = Solution()
# outcome = solution.convert_to_words_2(9992)
# print(outcome)