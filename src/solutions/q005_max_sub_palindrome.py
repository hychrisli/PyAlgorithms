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

    # Fastest approach
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


    # Center Expansion
    def longestPalindromev2(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        n = len(s)
        self.maxpalin = ""

        for i in xrange(n): # range from 0 to n-1
            self.expand(n,i,i) # odd len
            self.expand(n,i,i+1) # even len
        return self.maxpalin

    def expand(self,n, li, ui):

        while li > -1 and ui < n and self.s[li] == self.s[ui]:
            li -= 1
            ui += 1

        # step back
        li += 1
        ui -= 1

        if len(self.maxpalin) < ui - li + 1:
            self.maxpalin = self.s[li:ui+1]

    # First attempt DP -> Slow
    def longestPalindromev1(self, s):
        """
        Slow
        :type s: str
        :rtype: str
        """
        n = len(s)
        lkp = [[False for _ in xrange(n)] for _ in xrange(n)]
        maxsubstr = ""

        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                lkp[i][j] = s[i] == s[j] and ( j - i < 3 or lkp[i+1][j-1])
                if lkp[i][j] and j - i + 1 > len(maxsubstr):
                    maxsubstr = s[i:j+1]
        # for lst in lkp: print(lst)
        return maxsubstr


if __name__ == '__main__':
    sol = MaxSubPalindrome()
    sol.run_tests()

