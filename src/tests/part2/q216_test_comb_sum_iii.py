from src.base.test_cases import TestCases


class CombSumIiiTestCases(TestCases):

    def __init__(self):
        super(CombSumIiiTestCases, self).__init__()
        self.__add_test_case__("Test 1", (3, 7), [[1,2,4]])
        self.__add_test_case__("Test 2", (3, 9), [[1,2,6], [1,3,5], [2,3,4]])