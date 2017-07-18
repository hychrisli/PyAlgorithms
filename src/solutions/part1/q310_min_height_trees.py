from src.base.solution import Solution
from src.tests.part1.q310_test_min_height_trees import MinHeightTreesTestCases


class MinHeightTrees(Solution):
    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def print_output(self, output):
        super(MinHeightTrees, self).print_output(output)

    def gen_test_cases(self):
        return MinHeightTreesTestCases()

    def run_test(self, input):
        return self.findMinHeightTrees(input[0], input[1])

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1: return [0]

        graph = [set() for _ in xrange(n)]

        for i,j in edges:
            graph[i].add(j)
            graph[j].add(i)

        print(graph)

        leaves =[ i for i in xrange(n) if len(graph[i]) == 1]

        while n > 2:
            new_leaves = []
            n -= len(leaves)
            for leaf in leaves:
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                if len(graph[parent]) == 1:
                    new_leaves.append(parent)

            leaves = new_leaves
        return leaves

if __name__ == '__main__':
    sol = MinHeightTrees()
    sol.run_tests()