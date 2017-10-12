from src.base.solution import Solution
from src.tests.part2.q078_test_subsets import SubsetsTestCases

class Subsets(Solution):
    def gen_test_cases(self):
        return SubsetsTestCases()

    def run_test(self, input):
        return self.subsets(input)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            tailsets = []
            for subset in res:
                tailsets.append(subset + [num])
            res.extend(tailsets)
        return res


if __name__ == '__main__':
    sol = Subsets()
    sol.run_tests()