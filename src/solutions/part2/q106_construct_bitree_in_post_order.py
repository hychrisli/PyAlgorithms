from src.base.solution import Solution
from src.tests.part2.q106_test_construct_bitree_in_post_order import ConstructBiTreeInPostOrderTestCases
from src.structures.treenode import TreeNode

class ConstructBiTreeInPostOrder(Solution):
    def gen_test_cases(self):
        return ConstructBiTreeInPostOrderTestCases()

    def print_output(self, output):
        print(output.get_tree_str())

    def run_test(self, input):
        return self.buildTree(input[0], input[1])

    def verify_output(self, test_output, output):
        return test_output.get_tree_str() == output.get_tree_str()

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(ins, ine, pts, pte ):

            if ins > ine: return None

            root = TreeNode(postorder[pte])
            iroot = inorder.index(postorder[pte])

            jroot = iroot - ins + pts
            root.left = helper(ins, iroot - 1, pts, jroot - 1)
            root.right = helper(iroot + 1, ine, jroot, pte - 1)

            return root

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)



if __name__ == '__main__':
    sol = ConstructBiTreeInPostOrder()
    sol.run_tests()