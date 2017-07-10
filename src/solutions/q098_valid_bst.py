from src.base.solution import Solution
from src.tests.q098_test_valid_bst import ValidBstTestCases
import sys

class ValidBst(Solution):

    def verify_output(self, test_output, output):
        return test_output == output

    def run_test(self, input):
        return self.isValidBST(input)

    def print_output(self, output):
        super(ValidBst, self).print_output(output)

    def gen_test_cases(self):
        return ValidBstTestCases()

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = -sys.maxint
        return self.inorder_walk(root)


    def inorder_walk(self,root):

        if not root: return True

        if not self.inorder_walk(root.left):
            return False

        if root.val <= self.pre:
            return False
        else:
            self.pre = root.val

        if not self.inorder_walk(root.right):
            return False

        return True

if __name__ == '__main__':
    sol = ValidBst()
    sol.run_tests()