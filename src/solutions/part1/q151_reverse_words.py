from src.base.solution import Solution
from src.tests.part1.q151_test_reverse_words import ReverseWordsTestCases

"""

https://leetcode.com/problems/reverse-words-in-a-string/#/description

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

"""


class ReverseWords(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def run_test(self, input):
        return self.reverseWords(input)

    def gen_test_cases(self):
        return ReverseWordsTestCases()

    def print_output(self, output):
        super(ReverseWords, self).print_output(output)

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        words = s.split(' ')
        for word in words:
            if len(word) == 0:
                continue
            res = word + " " + res

        return res[:-1]

if __name__ == '__main__':
    solution = ReverseWords()
    solution.run_tests()