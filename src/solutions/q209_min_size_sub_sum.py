from src.base.solution import Solution
from src.tests.q209_test_min_size_sub_sum import MinSizeSubSumTestCases
import sys

class MinSizeSubSum(Solution):
    def print_output(self, output):
        super(MinSizeSubSum, self).print_output(output)

    def run_test(self, input):
        return self.minSubArrayLen(input[0], input[1])

    def gen_test_cases(self):
        return MinSizeSubSumTestCases()

    def verify_output(self, test_output, output):
        return test_output == output

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        nlen = len(nums)
        minlen = sys.maxint
        ssum = 0
        si = ei = 0

        while ei <= nlen:
            print(("before",ssum, si, ei))
            if ssum < s:
                if ei < nlen: ssum += nums[ei - 1]
                ei += 1
            else:
                minlen = min(minlen, ei - si)
                ssum -= nums[si]
                si += 1
            print(("after", ssum, si, ei))

        if minlen == sys.maxint: minlen = 0

        return minlen

if __name__ == '__main__':
    sol = MinSizeSubSum()
    sol.run_tests()