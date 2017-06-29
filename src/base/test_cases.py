import abc
from test_case import TestCase

class TestCases(list):
    name = "Generic Test"

    def __add_test_case__(self, *input, *output):
        self.append(TestCase(input, output))

    @staticmethod
    def __is_test_case__(test_case):
        return isinstance(test_case, TestCase)
