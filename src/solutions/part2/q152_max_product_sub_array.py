from src.base.solution import Solution
from src.tests.part2.q152_test_max_product_sub_array import MaxProductSubArrayTestCases
import sys

class MaxProductSubArray(Solution):
    def print_output(self, output):
        print(output)

    def gen_test_cases(self):
        return MaxProductSubArrayTestCases()

    def run_test(self, input):
        return self.maxProduct(input)

    def verify_output(self, test_output, output):
        return test_output == output

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxp = nums[0] if n else 0
        pre = (1, 1)
        # print(lkp)

        for i in xrange(n):
            val0 = pre[0] * nums[i]
            val1 = pre[1] * nums[i]
            imax = max(val0, max(val1, nums[i]))
            imin = min(val0, min(val1, nums[i]))
            pre = (imin, imax)
            maxp = max(maxp, pre[1])
        return maxp

if __name__ == '__main__':
    sol = MaxProductSubArray()
    sol.run_tests()