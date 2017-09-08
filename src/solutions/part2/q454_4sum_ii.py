from src.base.solution import Solution
from src.tests.part2.q454_test_4sum_ii import FourSumIiTestCases


class FourSumIi (Solution):
    def gen_test_cases(self):
        return FourSumIiTestCases()

    def run_test(self, input):
        return self.fourSumCount(input[0], input[1], input[2], input[3])

    def fourSumCount(self, A, B, C, D):
        from collections import defaultdict
        lkp = defaultdict(int)

        cnt = 0
        for va in A:
            for vb in B:
                lkp[va + vb] += 1

        for vc in C:
            for vd in D:
               if -vc-vd in lkp:
                   cnt += lkp[-vc-vd]

        return cnt


    def fourSumCountV1(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        lkpab, lkpcd = dict(), dict()

        cnt = 0
        for va in A:
            for vb in B:
                absum = va + vb
                lkpab[absum] = lkpab.get(absum, 0) + 1

        for vc in C:
            for vd in D:
                cdsum = vc + vd
                lkpcd[cdsum] = lkpcd.get(cdsum, 0) + 1

        for key in lkpab:
            if -key in lkpcd:
                cnt += lkpab[key] * lkpcd[-key]


        return cnt


if __name__ == '__main__':
    sol = FourSumIi()
    sol.run_tests()
