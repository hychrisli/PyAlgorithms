from src.base.solution import Solution
from src.tests.part2.q216_test_comb_sum_iii import CombSumIiiTestCases

class CombSumIii(Solution):
    def run_test(self, input):
        return self.combinationSum3(input[0], input[1])

    def gen_test_cases(self):
        return CombSumIiiTestCases()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        lkp = [0] * 10

        def helper(num, cnt, goal):

            if goal < num:
                return
            elif cnt == 1:
                if goal > num:
                    return
                elif goal == num:
                    lkp[num] = 1
                    res.append([x for x in xrange(1, 10) if lkp[x] == 1])
                    # print (res)
                    lkp[num] = 0
                    return

            lkp[num] = 1

            for x in xrange(num + 1, 10):
                helper (x, cnt - 1, goal - num)

            lkp[num] = 0
            return

        for x in xrange(1, 10):
            helper(x, k, n)


        return res


if __name__ == '__main__':
    sol = CombSumIii()
    sol.run_tests()
