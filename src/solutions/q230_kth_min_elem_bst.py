from src.base.solution import Solution
from src.tests.q230_test_kth_min_elem_bst import KthMinElemBstTestCases

class KthMinElemBst(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return KthMinElemBstTestCases()

    def run_test(self, input):
        return self.kthSmallest(input[0], input[1])

    def print_output(self, output):
        super(KthMinElemBst, self).print_output(output)


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.cnt = 0
        self.res = 0
        self.walk_nodes(root)

        return self.res

    def walk_nodes(self, root):

        if root:
            self.walk_nodes(root.left)
            # print(root.val)
            self.cnt += 1
            if self.cnt == self.k:
                self.res = root.val
                return
            self.walk_nodes(root.right)
        return

    def kthSmallestIterative(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = [root]
        num = 1
        visited = dict()
        visited[root] = True
        node = root
        while num <= k and stack:
            print((stack[-1].val, num))
            left_child = stack[-1].left
            if left_child and left_child not in visited:
                stack.append(left_child)
                visited[left_child] = True
            else:
                node = stack.pop()
                num += 1
                right_child = node.right
                if right_child and right_child not in visited:
                    stack.append(right_child)
                    visited[right_child] = True

        return node.val

if __name__ == '__main__':
    sol = KthMinElemBst()
    sol.run_tests()