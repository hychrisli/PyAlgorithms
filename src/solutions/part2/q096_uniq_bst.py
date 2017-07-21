from src.base.solution import Solution
from src.tests.part2.q096_test_uniq_bst import UniqueBstTestCases

class UniqBst(Solution):
    def run_test(self, input):
        return self.numTrees(input)

    def gen_test_cases(self):
        return UniqueBstTestCases()

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        lkp = [1,1]

        for i in xrange(2, n+1):
            res = 0
            for j in xrange(i):
                res += lkp[j] * lkp[i-j-1]
            lkp.append(res)

        return lkp[-1]

    def numTrees_2d(self, n):
        """
        :type n: int
        :rtype: int
        """
        lkp = [[1 for _ in xrange(n+2)] for _ in xrange(n+2) ]
        for i in xrange(1,n):
            lkp[i][i+1] = 2

        # print(lkp)
        for i in xrange(n-1, 0,-1):
            for j in xrange(i+2, n+1):
                res = 0
                for k in xrange(i, j+1):
                    res += lkp[i][k-1]*lkp[k+1][j]
                # print((i,j,res))
                lkp[i][j] = res

        return lkp[1][n]

if __name__ == '__main__':
    sol = UniqBst()
    sol.run_tests()