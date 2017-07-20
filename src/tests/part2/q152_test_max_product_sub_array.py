from src.base.test_cases import TestCases


class MaxProductSubArrayTestCases(TestCases):

    def __init__(self):
        super(MaxProductSubArrayTestCases,self).__init__()
        self.__add_test_case__('Test 1', [2, 3, -2, 4], 6)
        self.__add_test_case__('Test 2', [2, -3, -2, 4], 48)
        self.__add_test_case__('Test 3', [-2], -2)
        self.__add_test_case__('Test 4', [], 0)
        self.__add_test_case__('Test 5', [2, 0, 3], 3)
        self.__add_test_case__('Test 6', [0, 2], 2)