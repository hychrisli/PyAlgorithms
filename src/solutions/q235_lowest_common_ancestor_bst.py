from src.base.solution import Solution
from src.tests.q235_test_lowest_common_ancestor_bst import LowestCommonAncestorBstTestCases

class LowestCommonAncestorBst(Solution):
    def print_output(self, output):
        print(output)

    def run_test(self, input):
        return self.lowestCommonAncestor(input[0], input[1], input[2])

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return LowestCommonAncestorBstTestCases()

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print(root.to_str("", False))

        return False

if __name__ == '__main__':
    sol = LowestCommonAncestorBst()
    sol.run_tests()