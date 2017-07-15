from src.base.solution import Solution
from src.tests.q139_test_word_break import WordBreakTestCases

"""
https://leetcode.com/problems/word-break/#/description


Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

"""

class WordBreak(Solution):

    def gen_test_cases(self):
        return WordBreakTestCases()

    def run_test(self, input):
        return self.wordBreak(input[0], input[1])

    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        print(output)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wd = set(wordDict)
        n = len(s)
        lkp = [False for _ in xrange(n + 1)]
        lkp[0] = True


        for k in xrange(1, n + 1):
            i = 0
            while i < k and not lkp[k]:
                lkp[k] = lkp[i] and s[i:k] in wd
                i += 1

        # print(lkp)

        return lkp[-1]


if __name__ == '__main__':
    sol = WordBreak()
    sol.run_tests()
