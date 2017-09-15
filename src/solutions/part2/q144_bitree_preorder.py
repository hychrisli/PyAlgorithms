from src.base.solution import Solution
from src.tests.part2.q144_test_bitree_preorder import BitreePreOrderTestCases

class BitreePreOrder(Solution):
    def run_test(self, input):
        return self.preorderTraversal(input)

    def gen_test_cases(self):
        return BitreePreOrderTestCases()

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root: return []

        stk, res = [root], []

        while stk:

            node = stk.pop()
            res.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)

        return res


if __name__ == '__main__':

    sol = BitreePreOrder()
    sol.run_tests()