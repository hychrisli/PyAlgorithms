from src.base.solution import Solution
from src.tests.part2.q402_test_rm_k_digits import RmKDigitsTestCases

class RmKDigits(Solution):
    def gen_test_cases(self):
        return RmKDigitsTestCases()

    def run_test(self, input):
        return self.removeKdigits(input[0], input[1])

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stk, n, rn, j = [], len(num), len(num) - k, 0
        for i in xrange(n):

            # maintain stack such that top elem is less than incoming
            while j + k > i and stk and stk[-1] > num[i]:
                stk.pop()
                j -= 1
                # print ("after pop", stk)

            stk.append(num[i])
            j += 1
            # print stk
        res = ''.join(stk[:rn]).lstrip('0')

        return res if res else '0'

if __name__ == '__main__':
    sol = RmKDigits()
    sol.run_tests()
