from src.base.solution import Solution
from src.tests.q401_test_binary_watch import BinaryWatchTestCases

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

if __name__ == '__main__':
    sol = BinaryWatch()
    sol.run_tests()