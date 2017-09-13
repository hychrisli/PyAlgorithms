from src.base.solution import Solution
from src.tests.part2.q378_test_kth_elem_sorted_matrix import KthElemSortedMatrixTestCases


class KthElemSortedMatrix(Solution):
    def gen_test_cases(self):
        return KthElemSortedMatrixTestCases()

    def run_test(self, input):
        return self.kthSmallest(input[0], input[1])

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        lo, hi, m, n = matrix[0][0], matrix[-1][-1], len(matrix), len(matrix[0])

        print(m, n)
        while lo < hi:

            cnt, mid, j = 0, (lo + hi) / 2, n-1
            for i in xrange(m):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                cnt += j + 1

            if cnt < k:
                lo = mid + 1
            else:
                hi = mid

        return lo


    def kthSmallest_v1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq

        hq = matrix[0]

        for i in xrange(1, len(matrix)):
            hq += matrix[i]
        heapq.heapify(hq)
        for _ in xrange(k-1):
            heapq.heappop(hq)

        return hq[0]


if __name__ == '__main__':
    sol = KthElemSortedMatrix()
    sol.run_tests()