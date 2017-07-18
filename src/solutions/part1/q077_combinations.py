from src.base.solution import Solution
from src.tests.part1.q077_test_combinations import CombinationsTestCases

class Combinations(Solution):
    def gen_test_cases(self):
        return CombinationsTestCases()

    def run_test(self, input):
        return self.combine(input[0], input[1])

    def verify_output(self, test_output, output):
        print(str(test_output))
        tolst = [str(sorted(x)) for x in test_output]
        olst = [str(x) for x in output]
        return set(tolst) == set(olst)

    def print_output(self, output):
        print(output)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.subcombine(n, k, 1)

    def subcombine(self, n, k, sv):
        if k == 1:
            return [[x] for x in xrange(sv, n + 1)]
        res = []
        for i in xrange(sv, n - k + 2):
            subcb = self.subcombine(n, k - 1, i + 1)
            for x in subcb: x.append(i)
            # print((i, subcb))
            res.extend(subcb)
        return res

if __name__ == '__main__':
    sol = Combinations()
    sol.run_tests()