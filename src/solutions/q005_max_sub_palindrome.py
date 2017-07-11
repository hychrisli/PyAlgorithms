from src.base.solution import Solution
from src.tests.q005_test_max_sub_palindrome import MaxSubPalindromeTestCases

class MaxSubPalindrome(Solution):
    def gen_test_cases(self):
        return MaxSubPalindromeTestCases()

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        return self.longestPalindrome(input)

    def verify_output(self, test_output, output):
        return test_output in output

    def longestPalindrome(self, s):
        """

        :type s: str
        :rtype: str
        """
        n = len(s)
        lkp = [[False for _ in xrange(n)] for _ in xrange(n)]
        maxsubstr = ""

        for i in xrange(n):
            for j in xrange(i, n):
                lkp[i][j] = s[i] == s[j] and ( j - i < 3 or s[i+1] == s[j-1])
                if lkp[i][j] and j - i + 1 > len(maxsubstr):
                    maxsubstr = s[i:j+1]

        return maxsubstr


if __name__ == '__main__':
    sol = MaxSubPalindrome()
    sol.run_tests()

