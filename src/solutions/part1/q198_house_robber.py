from src.base.solution import Solution
from src.tests.part1.q198_test_house_robber import HouseRobberTestCases

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
        f(0) = nums[0]
        f(1) = max(num[0], num[1])
        f(k) = max( f(k-2) + nums[k], f(k-1) )
            use the node or not
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now

    def rob_v1(self, nums):
        """
        update date nums[i+2] with 2 or 3 houses ahead
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [0, 0] + nums

        for i in xrange(1, n):
            nums[i + 2] += max(nums[i],nums[i-1])

        return max(nums[-1], nums[-2])

if __name__ == '__main__':
    sol = HouseRobber()
    sol.run_tests()
