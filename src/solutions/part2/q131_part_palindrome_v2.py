from src.base.solution import Solution
from src.tests.part2.q131_test_part_palindrome import PartParlindromeTestCases


class PartPalindrome(Solution):
    def gen_test_cases(self):
        return PartParlindromeTestCases()

    def run_test(self, input):
        return self.partition(input)

    def verify_output(self, test_output, output):
        if len(test_output) != len(output) : return False

        res1 = set(['-'.join(sorted(lst)) for lst in test_output ])
        res2 = set(['-'.join(sorted(lst)) for lst in output ])
        # print res1
        return res1 == res2

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [[] for _ in xrange(n + 1)]
        dp[0].append([])
        print(dp)

        lkp = [[False] * len(s) for _ in xrange(n)]

        for j in xrange(n):
            for i in xrange(j+1):
                if s[i] != s[j]: continue
                if j - i < 3 or lkp[i+1][j-1]:
                    lkp[i][j] = True
                    for lst in dp[i]:
                        dp[j+1].append(lst + [s[i:j+1]])

        return dp[n]


if __name__ == '__main__':
    sol = PartPalindrome()
    sol.run_tests()