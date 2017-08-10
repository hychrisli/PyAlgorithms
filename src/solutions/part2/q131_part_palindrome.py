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
        self.lkp = [[None for _ in xrange(n)] for _ in xrange(n)]
        self.s = s
        return self.helper(0, n)

    def helper(self, si, n):
        if si >= n: return []

        res = []

        for j in xrange(si, n):
            if self.is_palindrome(si,j):
                nextlsts = self.helper(j + 1, n)

                if nextlsts:
                    for lst in nextlsts:
                        res.append([self.s[si:j+1]] + lst)
                else:
                    res.append([self.s[si:j+1]] )
        return res


    def is_palindrome(self, si, ei):
        if si >= ei: return True
        if self.lkp[si][ei] == None:
            if self.s[si] == self.s[ei]:
                self.lkp[si][ei] = self.is_palindrome(si + 1, ei - 1)
            else:
                self.lkp[si][ei] = False

        return self.lkp[si][ei]


if __name__ == '__main__':
    sol = PartPalindrome()
    sol.run_tests()