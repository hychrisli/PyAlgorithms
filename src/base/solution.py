import abc
from test_cases import TestCases
import sys

TEST_FAIL = 1

class Solution(object):
    __metaclass__ = abc.ABCMeta

    def run_tests(self):
        test_cases = self.gen_test_cases()

        for test_case in test_cases:
            test_output_tup = self.run_test(test_case.input_tup)
            if self.verify_output(test_output_tup, test_case.output_tup):
                self.__test_success__(test_case.name, test_output_tup)
            else:
                self.__test_fail__(test_case.name, test_output_tup)


    @abc.abstractmethod
    def gen_test_cases(self):
        """

        :return: list of test cases
        """
        return TestCases()

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
        return []

    def verify_output(self, test_output, output):
        """
        Verify if test output is valid compared to given output
        :param test_output: output of tests
        :param output: give output
        :return: True or False
        """
        return test_output == output

    def __test_success__(self, test_name, output_tup):
        """
        Handle successful test
        :param test_name: Name of the test case
        :return: N/A
        """
        print("[PASS] " + test_name)
        self.print_output(output_tup)

    def __test_fail__(self, test_name, output_tup):
        """
        Handle failed test
        :param test_name: Name of the test case
        :return: N/A
        """
        print("[FAIL] " + test_name)
        self.print_output(output_tup)
        sys.exit(TEST_FAIL)