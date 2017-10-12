from src.base.solution import Solution
from src.tests.part2.q059_test_spiral_matrix_ii import SpiralMatrixIiTestCases

class SpiralMatrix(Solution):
    def gen_test_cases(self):
        return SpiralMatrixIiTestCases()

    def run_test(self, input):
        return self.generateMatrix(input)

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        A = [[0]*n for _ in xrange(n)]
        x, y, dx, dy = 0, 0, 0, 1

        for i in xrange(n**2):
            A[x][y] = i + 1

            tx, ty = x+dx, y+dy

            if tx >= n or ty < 0 or ty >= n or A[tx][ty]:
                dx, dy = dy, -dx

            x += dx
            y += dy

        return A



if __name__ == '__main__':
    sol = SpiralMatrix()
    sol.run_tests()