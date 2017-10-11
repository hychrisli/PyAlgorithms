from src.base.solution import Solution
from src.tests.part2.q039_test_comb_sum import CombSumTestCases

class CombSum(Solution):
    def run_test(self, input):
        return self.combinationSum(input[0], input[1])

    def gen_test_cases(self):
        return CombSumTestCases()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res, comb = [], []

        def helper(idx, target, comb):

            if target < 0:
                return
            elif target == 0:
                res.append(comb)
                return

            for i in xrange(idx, len(candidates)):
                num = candidates[i]
                helper(i, target - num, comb + [num])

            return

        helper(0, target, [])

        return res


if __name__ == '__main__':
    sol = CombSum()
    sol.run_tests()