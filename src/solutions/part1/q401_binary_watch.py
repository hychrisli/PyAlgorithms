from src.base.solution import Solution
from src.tests.part1.q401_test_binary_watch import BinaryWatchTestCases

"""
https://leetcode.com/problems/binary-watch/#/description

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

"""


class BinaryWatch(Solution):
    def gen_test_cases(self):
        return BinaryWatchTestCases()

    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        return self.readBinaryWatch(input)

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hrs=[8, 4, 2, 1]
        mis=[32, 16, 8, 4, 2, 1]

        res = []

        for i in xrange(num + 1):
            hrc = self.__combine__(hrs, i, 0)
            mic = self.__combine__(mis, num - i, 0)
            for hr in hrc:
                for mi in mic:
                    if mi < 60 and hr < 12:
                        res.append('%d:%02d' % (hr, mi))

        return res


    def __combine__(self, lkp, n, si):
        if n == 0:
            return [0]

        if n == 1:
            return lkp[si:]

        res = []
        l = len(lkp)
        for i in xrange(si, l):
            lst = self.__combine__(lkp, n - 1, i + 1)
            lst = [x + lkp[i] for x in lst]
            res.extend(lst)

        return res

if __name__ == '__main__':
    sol = BinaryWatch()
    sol.run_tests()