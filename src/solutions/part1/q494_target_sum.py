from src.base.solution import Solution
from src.tests.part1.q494_test_target_sum import TargetSumTestCases

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
        return test_output == output

    def gen_test_cases(self):
        return TargetSumTestCases()

    def print_output(self, output):
        super(TargetSum, self).print_output(output)

    def run_test(self, input):
        return self.findTargetSumWays(input[0], input[1])

    def findTargetSumWays(self, nums, S):
        """
        The original problem statement is equivalent to:
        Find a subset of nums that need to be positive, and the rest of them negative,
        such that the sum is equal to target

        https://discuss.leetcode.com/topic/76243/java-15-ms-c-3-ms-o-ns-iterative-dp-solution-using-subset-sum-with-explanation

        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nsum = sum(nums)



    def findTargetSumWaysV1(self, nums, S):
        """
        DP traverse keys
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nlen = len(nums)
        if nlen < 1: return 0
        if nums[0] == 0:
            lkp = {nums[0]:2}
        else:
            lkp = {nums[0]:1, -nums[0]:1}

        idx = 1
        while idx < nlen:
            tmplkp = dict()
            for key in lkp:
                tmplkp[key + nums[idx]] = tmplkp.get(key + nums[idx], 0) + lkp[key]
                tmplkp[key - nums[idx]] = tmplkp.get(key - nums[idx], 0) + lkp[key]
            lkp = tmplkp

            # print(lkp)
            idx += 1

        if S in lkp:
            res = lkp[S]
        else:
            res = 0

        return res

if __name__ == '__main__':
    sol = TargetSum()
    sol.run_tests()