import sys

from src.base.solution import Solution
from src.tests.part1.q209_test_min_size_sub_sum import MinSizeSubSumTestCases

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ? s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


"""

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