from src.base.solution import Solution
from src.tests.q139_test_word_break import WordBreakTestCases

class WordBreak(Solution):
    def gen_test_cases(self):
        return WordBreakTestCases()

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        return self.wordBreak(input)

    def verify_output(self, test_output, output):
        return test_output == output

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """


if __name__ == '__main__':
    sol = WordBreak()
    sol.run_tests()