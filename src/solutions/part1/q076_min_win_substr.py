import sys

from src.base.solution import Solution
from src.tests.part1.q076_test_min_win_substr import MinWinSubStrTestCases


class MinWinSubStr(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        return self.minWindow(input[0], input[1])

    def gen_test_cases(self):
        return MinWinSubStrTestCases()

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        min_win, sl, cnt, head, si, ei = sys.maxint, len(s), len(t), 0, 0, 0
        lkp = {chr(x):0 for x in xrange(128)}
        for ch in t: lkp[ch] += 1
        # print(lkp)

        while ei < sl:
            # print((si, ei, min_win, cnt, s[si], s[ei]))
            if lkp[s[ei]] > 0: cnt -= 1
            lkp[s[ei]] -= 1
            ei += 1

            while cnt == 0:
                # print(('inner', si, ei, cnt))
                if min_win > ei - si:
                    min_win = ei - si
                    head = si
                if lkp[s[si]] == 0: cnt += 1
                lkp[s[si]] += 1
                si += 1

        return s[head: head + min_win] if min_win != sys.maxint else ''

if __name__ == '__main__':
    sol = MinWinSubStr()
    sol.run_tests()
