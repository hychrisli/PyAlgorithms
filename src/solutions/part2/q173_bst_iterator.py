from src.base.solution import Solution
from src.tests.part2.q173_test_bst_iterator import BstIterTestCases


class BstIteratorWrapper(Solution):
    def run_test(self, input):
        return self.get_sorted_res(input)

    def gen_test_cases(self):
        return BstIterTestCases()

    def get_sorted_res(self, root):

        class BSTIterator(object):

            def __init__(self, root):
                """
                :type root: TreeNode
                """
                self.stk = []
                if root:
                    self.stk.append(root)

            def hasNext(self):
                """
                :rtype: bool
                """
                if self.stk:
                    return True
                else:
                    return False

            def next(self):
                """
                :rtype: int
                """
                while self.stk[-1].left:
                    node = self.stk[-1]
                    self.stk.append(node.left)
                    node.left = None

                node = self.stk.pop()
                if node.right:
                    self.stk.append(node.right)

                return node.val

        it, res = BSTIterator(root), []

        while it.hasNext():
            res.append(it.next())

        return res


if __name__ == '__main__':
    sol = BstIteratorWrapper()
    sol.run_tests()
