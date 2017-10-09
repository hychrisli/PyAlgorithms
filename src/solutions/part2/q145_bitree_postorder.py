from src.base.solution import Solution
from src.tests.part2.q145_test_bitree_postorder import BiTreePostOrderTestCases


class BiTreePostOrder(Solution):
    def gen_test_cases(self):
        return BiTreePostOrderTestCases()

    def run_test(self, input):
        return self.postorderTraversal(input)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stk, res = [root], []
        while (stk):
            node = stk[-1]
            if not ( node.left or node.right ):
                stk.pop()
                res.append(node.val)
            else:
                if node.right:
                    stk.append(node.right)
                    node.right = None
                if node.left:
                    stk.append(node.left)
                    node.left = None
        return res


if __name__ == '__main__':
    sol = BiTreePostOrder()
    sol.run_tests()


