from src.base.solution import Solution
from src.tests.part2.q091_test_decode_ways import DecodeWaysTestCases

class DecodeWays(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def run_test(self, input):
        return self.numDecodings(input)

    def gen_test_cases(self):
        return DecodeWaysTestCases()

    def print_output(self, output):
        print(output)

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre,n = 9, len(s)
        if not n: return 0
        res = [0] * (n+1)
        res[0] = 1

        for i in xrange(n):
            val = int(s[i])
            if pre == 1 or (pre == 2 and val < 7):
                if val == 0:
                    res[i+1] = res[i-1]
                else:
                    res[i+1] = res[i] + res[i-1]
            else:
                if val == 0:
                    res[i+1] = 0
                else:
                    res[i+1] = res[i]
            pre = val

        return res[n]

if __name__ == '__main__':
    sol = DecodeWays()
    sol.run_tests()
