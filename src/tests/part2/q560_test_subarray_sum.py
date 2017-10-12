from src.base.test_cases import TestCases


class SubArraySumTestCases(TestCases):

    def __init__(self):
        super(SubArraySumTestCases, self).__init__()
        self.__add_test_case__('Test 1', ([1,1,1], 2), 2)
        self.__add_test_case__('Test 2', ([1,2,1,2], 3), 3)
        self.__add_test_case__('Test 3', ([1, -1, 1, 2], 2), 2)
        self.__add_test_case__('Test 4', ([1, -1, 1, 1, 1, -1, 1], 2), 8)