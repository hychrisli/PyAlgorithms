from src.base.solution import Solution
from src.tests.part2.q449_test_de_serial_bst import DeSerialBstTestCases

class DeSerialBst(Solution):
    def run_test(self, input):
        code = Codec()
        retur

    def gen_test_cases(self):
        return DeSerialBstTestCases()

    def verify_output(self, test_output, output):
        return super(DeSerialBst, self).verify_output(test_output, output)

    def print_output(self, output):
        super(DeSerialBst, self).print_output(output)


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    sol = DeSerialBst()
    sol.run_tests()
