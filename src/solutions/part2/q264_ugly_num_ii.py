from src.base.solution import Solution
from src.tests.part2.q264_test_ugly_num_ii import UglyNumTestCases

class UglyNumIi(Solution):

    def gen_test_cases(self):
        return UglyNumTestCases()

    def run_test(self, input):
        return self.nthUglyNumber(input)

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        import heapq

        pq, cnt, val, lkp = [1], 0, None, dict()

        while pq and cnt < n:
            val = heapq.heappop(pq)
            cnt += 1
            val2 = val*2
            val3 = val*3
            val5 = val*5
            if val2 not in lkp:
                heapq.heappush(pq, val2)
                lkp[val2] = True

            if val3 not in lkp:
                heapq.heappush(pq, val3)
                lkp[val3] = True

            if val5 not in lkp:
                heapq.heappush(pq, val5)
                lkp[val5] = True

            # print(pq)

        return val



if __name__ == '__main__':
    sol = UglyNumIi()
    sol.run_tests()