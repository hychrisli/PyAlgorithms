from src.base.solution import Solution
from src.tests.part2.q105_test_construct_bitree_pre_in_order import ConstructBiTreePreInOrderTestCases
from src.structures.treenode import TreeNode

class ConstructBiTreePreInOrder(Solution):
    def print_output(self, output):
        print(output.get_tree_str())

    def gen_test_cases(self):
        return ConstructBiTreePreInOrderTestCases()

    def run_test(self, input):
        return self.buildTree(input[0], input[1])

    def verify_output(self, test_output, output):
        return test_output.get_tree_str() == output.get_tree_str()

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder

        self.lkp = { val:idx for idx, val in enumerate(inorder)}

        return self.builder(0, len(preorder) - 1, 0)

    def builder(self, insi, inei, preidx):

        if insi > inei: return None

        idx = self.lkp[self.preorder[preidx]]

        """while self.inorder[idx] != self.preorder[preidx]:
            idx += 1"""

        node = TreeNode(self.preorder[preidx])
        node.left = self.builder(insi, idx - 1, preidx + 1)
        node.right = self.builder(idx + 1, inei, preidx + idx - insi + 1)

        return node


if __name__ == '__main__':
    sol = ConstructBiTreePreInOrder()
    sol.run_tests()