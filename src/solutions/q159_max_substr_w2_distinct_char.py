from src.base.solution import Solution
from src.tests.q159_test_max_substr_w2_distinct_char import MaxSubStrW2DistinctCharTestCases

"""

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

Given a string, find the longest substring that contains only two unique characters. For example, given "abcbbbbcccbdddadacb", 
the longest substring that contains 2 unique character is "bcbbbbcccb".

"""

class MaxSubStrW2DistinctChar(Solution):
    def run_test(self, input):
        return self.len_substr_two_distinct(input)

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return MaxSubStrW2DistinctCharTestCases()

    def len_substr_two_distinct(self, s):
        """

        :type s: str
        :rtype: int
        """

        lkp = {chr(x):0 for x in xrange(128)}
        si, ei, cnt, maxlen, n = 0, 0, 0, 0, len(s)

        while ei < n:
            if lkp[s[ei]] == 0:
                cnt += 1
            lkp[s[ei]] += 1
            ei += 1

            # print((s[si:ei], si, ei, cnt))

            while cnt > 2:
                if lkp[s[si]] == 1: cnt -= 1
                lkp[s[si]] -= 1
                si += 1

            maxlen = max(ei - si, maxlen)


        return maxlen

if __name__ == '__main__':
    sol = MaxSubStrW2DistinctChar()
    sol.run_tests()
