from src.base.solution import Solution
from src.tests.part2.q104_test_max_bi_tree_depth import MaxBiTreeDepthTestCases


class MaxBiTreeDepth(Solution):
    def gen_test_cases(self):
        return MaxBiTreeDepthTestCases()

    def run_test(self, input):
        return self.maxDepth(input)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



if __name__ == '__main__':
    sol = MaxBiTreeDepth()
    sol.run_tests()