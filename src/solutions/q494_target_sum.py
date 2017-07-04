from src.base.solution import Solution
from src.tests.q494_test_target_sum import TargetSumTestCases

"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.


"""


class TargetSum(Solution):
    def verify_output(self, test_output, output):
        return super(TargetSum, self).verify_output(test_output, output)

    def gen_test_cases(self):
        return super(TargetSum, self).gen_test_cases()

    def print_output(self, output):
        super(TargetSum, self).print_output(output)

    def run_test(self, input):
        return super(TargetSum, self).run_test(input)

    class Solution(object):
        def findTargetSumWays(self, nums, S):
            """
            :type nums: List[int]
            :type S: int
            :rtype: int
            """

if __name__ == '__main__':
    sol = TargetSum()
    sol.run_tests()