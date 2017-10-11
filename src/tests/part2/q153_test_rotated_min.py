from src.base.test_cases import TestCases


class RotatedMinTestCases(TestCases):
    def __init__(self):
        super(RotatedMinTestCases, self).__init__()
        self.__add_test_case__("Test 1", [4, 5, 6, 7, 0, 1, 2], 0)
        self.__add_test_case__("Test 2", [2, 3, 4, 5, 6, 7, 8, 9, 1], 1)
        self.__add_test_case__("Test 3", [3, 4], 3)
        self.__add_test_case__("Test 4", [4], 4)
        self.__add_test_case__("Test 5", [7, 8, 1, 2, 3, 4, 5, 6], 1)
        self.__add_test_case__("Test 6", [7, 1, 2], 1)
