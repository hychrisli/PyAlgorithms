from src.base.solution import Solution
from src.tests.part2.q529_test_mine_sweeper import MineSweeperTestCases


class MineSweeper(Solution):
    def run_test(self, input):
        return self.updateBoard(input[0], input[1])

    def gen_test_cases(self):
        return MineSweeperTestCases()

    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.m, self.n, self.board = len(board), len(board[0]), board
        self.bound = {'B', 'M', '1', '2', '3', '4', '5', '6', '7', '8'}
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        self.helper(click[0], click[1])
        return self.board


    def helper(self, r, c):

        if r in {-1, self.m} or c in {-1, self.n} or self.board[r][c] in self.bound:
            return
        cnt = self.getMines(r,c)

        if cnt: self.board[r][c] = str(cnt)
        else:
            self.board[r][c] = 'B'
            for i in xrange(r-1, r+2):
                for j in xrange(c-1, c+2):
                    self.helper(i,j)


    def getMines(self, r, c):
        cnt = 0
        for i in xrange(r-1, r+2):
            for j in xrange(c-1, c+2):
                if i in {-1, self.m} or j in {-1, self.n}:
                    continue
                if self.board[i][j] == 'M':
                    cnt += 1

        return cnt



if __name__ == '__main__':
    sol = MineSweeper()
    sol.run_tests()