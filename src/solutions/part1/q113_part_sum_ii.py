from src.base.solution import Solution
from src.tests.part1.q113_test_part_sum_ii import PartSumIITestCases

class PartSumII(Solution):
    def gen_test_cases(self):
        return PartSumIITestCases()

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        oset = set()
        for lst in output:
            oset.add('-'.join(str(x) for x in lst))

        toset = set()
        for lst in test_output:
            toset.add('-'.join(str(x) for x in lst))

        return oset == toset

    def run_test(self, input):
        return self.pathSum(input[0], input[1])

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.path_vals = []
        self.res = []
        self.target_sum = sum
        self.__sub_path__(root, 0)
        return self.res

    def __sub_path__(self, root, sub_sum):

        if root == None:
            return

        self.path_vals.append(root.val)
        sub_sum += root.val

        if root.left == None and root.right == None:
            if sub_sum == self.target_sum:
                self.res.append([x for x in self.path_vals])

            self.path_vals.pop()
            return

        self.__sub_path__(root.left, sub_sum)
        self.__sub_path__(root.right, sub_sum)
        self.path_vals.pop()
        return



if __name__ == '__main__':
    sol = PartSumII()
    sol.run_tests()