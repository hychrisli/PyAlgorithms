from src.base.solution import Solution
from src.tests.part2.q120_test_triangle import TriangleTestCases


class Triangle(Solution):
    def run_test(self, input):
        return self.minimumTotal(input)

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return TriangleTestCases()

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        nrow = len(triangle)
        ncol = nrow - 1

        while ncol:
            for j in xrange(ncol):
                triangle[ncol - 1][j] += min(triangle[ncol][j],triangle[ncol][j+1])
            ncol -= 1
        # print(triangle)

        return triangle[0][0]

if __name__ == '__main__':
    sol = Triangle()
    sol.run_tests()