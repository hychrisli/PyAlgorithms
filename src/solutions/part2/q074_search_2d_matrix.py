from src.base.solution import Solution
from src.tests.part2.q074_test_search_2d_matrix import Search2dMatrixTestCases

class Search2dMatrix(Solution):
    def gen_test_cases(self):
        return Search2dMatrixTestCases()

    def run_test(self, input):
        return self.searchMatrix(input[0], input[1])

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        m, n= len(matrix), len(matrix[0])
        sr, er = 0, m-1
        # print(sr, er)

        if target >= matrix[m-1][0]:
            sr = m-1
        else:
            while sr < er - 1:
                mid = (sr + er) / 2
                if target == matrix[mid][0]:
                    return True

                if target < matrix[mid][0]:
                    er = mid
                else:
                    sr = mid
        # print(sr, er)

        sc, ec = 0, n-1

        while sc <= ec:
            # print("col", sc, ec)
            mid = (sc + ec) / 2
            if target == matrix[sr][mid]:
                return True

            if target < matrix[sr][mid]:
                ec = mid - 1
            else:
                sc = mid + 1


        return False


if __name__ == '__main__':
    sol = Search2dMatrix()
    sol.run_tests()