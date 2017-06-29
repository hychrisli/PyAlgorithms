import abc
from test_cases import TestCases
import sys

TEST_FAIL = 1

class Solution(object):
    __metaclass__ = abc.ABCMeta

    def run_tests(self):
        test_cases = self.gen_test_cases()

        for test_case in test_cases:
            test_output = self.run_test(test_case.input)
            if not self.verify_output(test_output, test_case.output):
                self.test_success(test_case.name)
            else:
                self.test_fail(test_case.name)


    @abc.abstractmethod
    def gen_test_cases(self):
        """

        :return: list of test cases
        """
        return TestCases()

    @abc.abstractmethod
    def print_output(self, output):
        """
        print output data
        :param output: output data
        :return: N/A
        """
        print(output)

    @abc.abstractmethod
    def run_test(self, input):
        """
        specify how to run a test
        :param input: input value
        :return: return test output
        """
        pass

    @abc.abstractmethod
    def verify_output(self, test_output, output):
        """
        Verify if test output is valid compared to given output
        :param test_output: output of tests
        :param output: give output
        :return: True or False
        """
        if test_output == output:
            return True

        return False


    @staticmethod
    def test_success(test_name):
        """
        Handle successful test
        :param test_name: Name of the test case
        :return: N/A
        """
        print("[PASS] " + test_name)

    @staticmethod
    def test_fail(test_name):
        """
        Handle failed test
        :param test_name: Name of the test case
        :return: N/A
        """
        print("[FAIL] " + test_name)
        sys.exit(TEST_FAIL)