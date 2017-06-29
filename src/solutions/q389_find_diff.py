from src.base.solution import Solution
from src.tests.q389_test_find_diff import FindDiffTestCases

class FindDiff(Solution):
    def verify_output(self, test_output, output):
        return test_output[0] == output[0]

    def run_test(self, input):
        return self.findTheDifference(input[0], input[1])

    def gen_test_cases(self):
        return FindDiffTestCases()

    def print_output(self, output):
        super(FindDiff, self).print_output(output)

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lkp = dict()

        for ch in s:
            lkp[ch] = lkp.get(ch, 0) + 1

        for ch in t:
            lkp[ch] = lkp.get(ch, 0) - 1
            if lkp[ch] < 0:
                return ch


if __name__ == '__main__':
    solution = FindDiff()
    solution.run_tests()