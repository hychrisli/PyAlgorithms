from src.base.solution import Solution
from src.tests.q064_test_min_path_sum import MinPathSumTestCases

class MinPathSum(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def run_test(self, input):
        return self.minPathSum(input)

    def gen_test_cases(self):
        return MinPathSumTestCases()

    def print_output(self, output):
        print(output)

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m < 1: return 0
        n = len(grid[0])
        if n < 1: return 0

        for i in xrange(1,m):
            grid[i][0] += grid[i-1][0]
        for j in xrange(1,n):
            grid[0][j] += grid[0][j-1]

        for i in xrange(1,m):
            for j in xrange(1,n):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])

        return grid[m-1][n-1]

if __name__ == '__main__':
    sol = MinPathSum()
    sol.run_tests()
