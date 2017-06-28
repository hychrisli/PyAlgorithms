import abc
from test_cases import TestCases
import sys

TEST_FAIL = 1

class Solution(object):

    def runTests(self):
        test_cases = self.gen_test_cases()

        for test_case in test_cases:
            test_output = self.run_tests(test_case.input)
            if not self.verify_output(test_output, test_case.output):
                self.test_success(test_case.name)
            else:
                self.test_fail(test_case.name)


    @abc.abstractmethod
    def gen_test_cases(self):
        return TestCases()

    @abc.abstractmethod
    def print_out_data(self, output):
        pass

    @abc.abstractmethod
    def run_tests(self, input):
        pass

    @abc.abstractmethod
    def verify_output(self, test_output, output):
        return False


    @staticmethod
    def test_success(test_name):
        print("[PASS] " + test_name)

    @staticmethod
    def test_fail(test_name):
        print("[FAIL] " + test_name)
        sys.exit(TEST_FAIL)