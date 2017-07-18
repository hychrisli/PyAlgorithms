from src.base.solution import Solution
from src.tests.part1.q416_test_part_equal_sub_sum import PartEqualSubSumTestCases

"""
https://leetcode.com/problems/partition-equal-subset-sum/#/description

Given a non-empty array containing only positive integers, 
    find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""


class PartEqualSubSum(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return PartEqualSubSumTestCases()

    def print_output(self, output):
        super(PartEqualSubSum, self).print_output(output)

    def run_test(self, input):
        return self.canPartition(input)

    def canPartition(self, nums):
        """
        https://discuss.leetcode.com/topic/67539/0-1-knapsack-detailed-explanation
        :type nums: List[int]
        :rtype: bool
        """

        nsum = sum(nums)
        if nsum % 2:
            return False

        nsum /= 2
        lkp = [False]*(nsum + 1)
        lkp[0] = True

        for num in nums:
            for i in xrange(nsum, 0, -1):
                lkp[i] = lkp[i] or ( lkp[i-num] if i-num >= 0 else False )

        return lkp[-1]


if __name__ == '__main__':
    sol = PartEqualSubSum()
    sol.run_tests()