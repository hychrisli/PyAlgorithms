from test_case import TestCase

class TestCases(list):
    name = "Generic Test"

    def __add_test_case__(self, name, input_tup, output_tup):
        self.append(TestCase(name, input_tup, output_tup))

    @staticmethod
    def __is_test_case__(test_case):
        return isinstance(test_case, TestCase)
