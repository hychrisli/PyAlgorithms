from src.base.solution import Solution
from src.tests.part2.q092_test_bitree_inorder import BitreeInorderTestCases

class BitreeInorder(Solution):
    def gen_test_cases(self):
        return BitreeInorderTestCases()

    def run_test(self, input):
        return self.inorderTraversal(input)

    def inorderTraversal(self, root):

        res = []
        if root:
            stk = [root]
            while stk:
                lnode = stk[-1].left
                if lnode :
                    stk[-1].left = None
                    stk.append(lnode)
                else:
                    node = stk.pop()
                    res.append(node.val)
                    rnode = node.right
                    if rnode:
                        stk.append(rnode)
        return res


    def inorderTraversal_v1(self, root):
        """
        recursive
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def walk(root):
            if not root: return

            walk(root.left)
            res.append(root.val)
            walk(root.right)

        walk(root)

        return res


if __name__ == '__main__':
    sol = BitreeInorder()
    sol.run_tests()

