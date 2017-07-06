from src.base.solution import Solution
from src.tests.q310_test_min_height_trees import MinHeightTreesTestCases


class MinHeightTrees(Solution):
    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def print_output(self, output):
        super(MinHeightTrees, self).print_output(output)

    def gen_test_cases(self):
        return MinHeightTreesTestCases()

    def run_test(self, input):
        return self.findMinHeightTrees(input[0], input[1])

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        return []


if __name__ == '__main__':
    sol = MinHeightTrees()
    sol.run_tests()