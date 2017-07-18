from src.base.solution import Solution
from src.tests.hacker.test_cipher import CipherTestCases

"""
https://www.hackerrank.com/challenges/cipher/problem

"""

class Cipher(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        print(output)

    def gen_test_cases(self):
        return CipherTestCases()

    def run_test(self, input):
        return self.getcode(input[0], input[1], input[2])

    def getcode(self, n, k, s):

        woxr, res, ord0 = 0, [], ord('0')

        for i in xrange(n):

            if i >= k:
                woxr ^= ord(res[i-k]) - ord0
            val = (ord(s[i]) - ord0 ) ^ woxr
            res.append(chr(val + ord0))
            woxr ^= val

        return ''.join(res)


    def getcode_v1(self, n, k, s):

        """
        Too slow O(n*k)

        :param n:
        :param k:
        :param s:
        :return:
        """

        sl = len(s)
        si, ei, lnl, rnl = 0, sl - 1, [], []

        while si < ei:

            ln, i, ki = int(s[si]), si, k - 1
            while min(i, ki) > 0:
                ln ^= lnl[i - 1]
                i -= 1
                ki -= 1
            lnl.append(ln)
            si += 1

            rn, j, kj = int(s[ei]), sl - ei - 1, k - 1
            while min(j, kj) > 0:
                rn ^= rnl[j - 1]
                j -= 1
                kj -= 1
            rnl.append(rn)
            ei -= 1

            # print((si, lnl, ei, rnl))

        res = lnl[:n / 2 + 1]
        res.extend(reversed(rnl[: n / 2]))

        return ''.join(str(x) for x in res)

if __name__ == '__main__':
    sol = Cipher()
    sol.run_tests()