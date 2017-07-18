from src.base.solution import Solution
from src.tests.part2.q179_test_max_num import MaxNumTestCases

"""
https://leetcode.com/submissions/detail/110156821/
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.


"""

class MaxNum(Solution):

    def gen_test_cases(self):
        return MaxNumTestCases()

    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        return self.largestNumber(input)

    def largestNumber(self, nums):
        numstrs = [str(x) for x in nums]
        numstrs.sort(cmp=lambda x, y: cmp(x+y, y+x), reverse=True)
        return "".join(numstrs).lstrip('0') or '0'


if __name__ == '__main__':
    sol = MaxNum()
    sol.run_tests()