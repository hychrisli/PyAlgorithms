from src.base.test_cases import TestCases

class MaxNumTestCases(TestCases):

    def __init__(self):
        super(MaxNumTestCases, self).__init__()
        self.__add_test_case__('Test 1', [3, 30, 34, 5, 9], "9534330")
        self.__add_test_case__('Test 1', [0, 0], '0')