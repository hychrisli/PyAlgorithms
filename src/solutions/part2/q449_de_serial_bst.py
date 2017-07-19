from src.base.solution import Solution
from src.tests.part2.q449_test_de_serial_bst import DeSerialBstTestCases
from src.structures.treenode import TreeNode

class DeSerialBst(Solution):
    def run_test(self, input):
        serial_bst = Codec()
        res1 = serial_bst.serialize(input[0])
        res2 = serial_bst.deserialize(input[1])
        return (res1, res2)

    def gen_test_cases(self):
        return DeSerialBstTestCases()

    def verify_output(self, test_output, output):
        return test_output[0] == output[0] and test_output[1] == output[1]

    def print_output(self, output):
        print((output[0], output[1].get_tree_str()))

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.vals = []
        self.preorder_serial(root)
        return ' '.join(self.vals)

    def preorder_serial(self, root):
        if not root:
            self.vals.append('n')
            return
        # print(self.vals)
        self.vals.append(str(root.val))
        self.preorder_serial(root.left)
        self.preorder_serial(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.chs = data.split(' ')
        self.n = len(self.chs)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    sol = DeSerialBst()
    sol.run_tests()
