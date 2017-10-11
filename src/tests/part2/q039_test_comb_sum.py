from src.base.test_cases import TestCases


class CombSumTestCases(TestCases):

    def __init__(self):
        super(CombSumTestCases, self).__init__()
        self.__add_test_case__("Test 1", ([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.__add_test_case__("Test 2", ([2, 3, 5, 6, 9], 8), [[2, 2, 2, 2], [2, 3, 3], [2, 6], [3, 5]])
