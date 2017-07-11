from src.base.solution import Solution
from src.tests.q198_test_house_robber import HouseRobberTestCases

class HouseRobber(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        return self.rob(input)

    def gen_test_cases(self):
        return HouseRobberTestCases()

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [0, 0] + nums

        for i in xrange(n):
            nums[i + 2] += nums[i]

        return max(nums[-1], nums[-2])

if __name__ == '__main__':
    sol = HouseRobber()
    sol.run_tests()
