from src.base.solution import Solution
from src.tests.part1.q235_test_lowest_common_ancestor_bst import LowestCommonAncestorBstTestCases

class LowestCommonAncestorBst(Solution):
    def print_output(self, output):
        print(output.val if output else None)

    def run_test(self, input):
        return self.lowestCommonAncestor(input[0], input[1], input[2])

    def verify_output(self, test_output, output):
        return test_output.val if test_output else None == output.val if output else None

    def gen_test_cases(self):
        return LowestCommonAncestorBstTestCases()

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # print(root.to_str("", False))

        while  (root.val - p.val) * (root.val - q.val) > 0:
            # print root.val
            root = (root.left, root.right)[p.val > root.val]

        return root

if __name__ == '__main__':
    sol = LowestCommonAncestorBst()
    sol.run_tests()