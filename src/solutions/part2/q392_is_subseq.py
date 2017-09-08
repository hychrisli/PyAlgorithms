from src.base.solution import Solution
from src.tests.part2.q392_test_is_subseq import IsSubSeqTestCases

class IsSubSeq (Solution):
    def gen_test_cases(self):
        return IsSubSeqTestCases()

    def run_test(self, input):
        return self.isSubsequence(input[0], input[1])

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx, n = 0, len(s)

        if not n: return True

        for ch in t:
            if ch == s[idx]:
                idx += 1
                if idx == n:
                    return True
        return False



if __name__ == '__main__':

    sol = IsSubSeq()
    sol.run_tests()