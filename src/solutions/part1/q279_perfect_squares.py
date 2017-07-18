import collections
import math

from src.base.solution import Solution
from src.tests.part1.q279_test_perfect_squares import PerfectSquaresTestCases


class PerfectSquares(Solution):
    def print_output(self, output):
        super(PerfectSquares, self).print_output(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return PerfectSquaresTestCases()

    def run_test(self, input):
        return self.numSquares(input)

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        class Node:
            def __init__(self, val, dist):
                self.val = val
                self.dist = dist

        node_dict = dict()
        q = collections.deque()
        min_dist = n
        q.append(Node(n, 0))
        node_dict[(n,0)] = True

        while q:
            cur_node = q.popleft()
            val_sqrt = math.floor(math.sqrt(cur_node.val))

            while val_sqrt:
                val = cur_node.val - val_sqrt**2
                dist = cur_node.dist + 1
                val_sqrt -= 1

                if val == 0 and dist < min_dist:
                    min_dist = dist
                    # print([val, val_sqrt, dist])
                    continue

                if val < 0 or dist >= min_dist:
                    continue

                if (val, dist) not in node_dict:
                    q.append(Node(val, dist))
                    node_dict[(val,dist)] = True
                    # print([(x.val, x.dist) for x in q])

        return min_dist


if __name__ == '__main__':
    sol = PerfectSquares()
    sol.run_tests()