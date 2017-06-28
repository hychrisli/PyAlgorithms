import abc
from test_case import TestCase

class TestCases(list):
    name = "Generic Test"

    @abc.abstractmethod
    def add_test_case(self, test_case):
        pass

    @staticmethod
    def is_test_case(test_case):
        return isinstance(test_case, TestCase)
