from src.base.solution import Solution
from src.tests.part2.q200_test_island_num import IslandNumTestCases

class IslandNum(Solution):
    def run_test(self, input):
        return self.numIslands(input)

    def gen_test_cases(self):
        return IslandNumTestCases()

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = [[ch for ch in s] for s in grid]
        cnt = 0
        self.m = len(grid)
        if not self.m: return 0
        self.n = len(grid[0])

        # print (self.grid)

        for i in xrange(self.m):
            for j in xrange(self.n):
                if self.grid[i][j] == '1':
                    cnt += 1
                    self.dfs(i,j)
        return cnt

    def dfs(self, i,j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.grid[i][j] == '0': return
        self.grid[i][j] = '0'
        self.dfs(i-1, j)
        self.dfs(i, j-1)
        self.dfs(i, j+1)
        self.dfs(i+1, j)


if __name__ == '__main__':
    sol = IslandNum()
    sol.run_tests()