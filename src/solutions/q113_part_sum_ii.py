from src.base.solution import Solution
from src.tests.q113_test_part_sum_ii import PartSumIITestCases

class PartSumII(Solution):
    def gen_test_cases(self):
        return PartSumIITestCases()

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        oset = set()
        for lst in output:
            oset.add('-'.join(str(x) for x in lst))

        toset = set()
        for lst in test_output:
            toset.add('-'.join(str(x) for x in lst))

        return oset == toset

    def run_test(self, input):
        return self.pathSum(input[0], input[1])

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        print(root.get_tree_str())

        return [[1]]


if __name__ == '__main__':
    sol = PartSumII()
    sol.run_tests()