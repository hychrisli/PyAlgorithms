from src.base.solution import Solution
from src.tests.q310_test_min_height_trees import MinHeightTreesTestCases
import collections


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
        graph = dict()

        for i,j in edges:
            graph[i] = graph.get(i,set())
            graph[i].add(j)
            graph[j] = graph.get(j,set())
            graph[j].add(i)

        leaves = collections.deque([ i for i in xrange(n) if len(graph[i]) == 1])

        while leaves:
            print(leaves)
            print(graph)
            leaf = leaves.popleft()
            if graph[leaf]:
                parent = graph[leaf].pop()
                if len(graph[parent]) == 1 and leaf in graph[parent]:
                    return [parent, leaf]
                graph[parent].remove(leaf)
                if len(graph[parent]) < 2:
                    leaves.append(parent)
            else:
                return [leaf]


if __name__ == '__main__':
    sol = MinHeightTrees()
    sol.run_tests()