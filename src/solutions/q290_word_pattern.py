from src.base.solution import Solution
from src.tests.q290_test_word_pattern import WordPatternTestCases

"""
https://leetcode.com/problems/word-pattern/#/description

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

"""


class WordPattern(Solution):
    def verify_output(self, test_output, output):
        return super(WordPattern, self).verify_output(test_output, output)

    def run_test(self, input):
        return self.wordPattern(input[0], input[1])

    def gen_test_cases(self):
        return WordPatternTestCases()

    def print_output(self, output):
        super(WordPattern, self).print_output(output)

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
