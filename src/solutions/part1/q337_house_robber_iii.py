from src.base.solution import Solution
from src.tests.part1.q337_test_house_robber_iii import HouseRobberIIITestCases

class HouseRobberIII(Solution):
    def print_output(self, output):
        super(HouseRobberIII, self).print_output(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return HouseRobberIIITestCases()

    def run_test(self, input):
        return self.rob(input)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.lkp = dict()
        return self.sub_rob(root)


    def sub_rob(self, root):
        if not root: return 0
        if root in self.lkp: return self.lkp[root]
        gcval = 0
        if root.left:
            gcval += self.sub_rob(root.left.left) + self.sub_rob(root.left.right)

        if root.right:
            gcval += self.sub_rob(root.right.left) + self.sub_rob(root.right.right)

        self.lkp[root] = max(gcval + root.val,  self.sub_rob(root.left) + self.sub_rob(root.right))

        # print([(k.val, v) for k,v in self.lkp.iteritems()])

        return self.lkp[root]


    """
    First Attempt
    """

    def rob_v1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.clkp = dict()
        self.gclkp = dict()

        return self.c_helper(root)

    def c_helper(self, root):

        if not root:
            return 0

        if root in self.clkp:
            return self.clkp[root]

        csum = self.c_helper(root.left) + self.c_helper(root.right)
        gcsum = self.gc_helper(root.left) + self.gc_helper(root.right)

        self.gclkp[root] = csum
        self.clkp[root] = gcsum + root.val

        return max(self.gclkp[root], self.clkp[root])

    def gc_helper(self, root):
        if not root:
            return 0

        if root in self.gclkp:
            return self.gclkp[root]

        return self.gc_helper(root.left) + self.gc_helper(root.right)


if __name__ == '__main__':
    sol = HouseRobberIII()
    sol.run_tests()
