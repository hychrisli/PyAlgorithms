from src.base.solution import Solution
from src.tests.part2.q560_test_subarray_sum import SubArraySumTestCases

class SubArraySum(Solution):
    def run_test(self, input):
        return self.subarraySum(input[0], input[1])

    def gen_test_cases(self):
        return SubArraySumTestCases()

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        lkp, sum, cnt = {0:1}, 0, 0

        for num in nums:
            sum += num
            cnt += lkp.get(sum - k, 0)
            # print(sum, num, cnt, sum - k)
            # print(lkp)
            lkp[sum] = lkp.get(sum, 0) + 1

        return cnt


if __name__ == '__main__':
    sol = SubArraySum()
    sol.run_tests()