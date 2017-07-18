from src.base.test_cases import TestCases

class MinSizeSubSumTestCases(TestCases):
    def __init__(self):
        super(MinSizeSubSumTestCases, self).__init__()
        self.__add_test_case__("Example 1", (7, [2,3,1,2,4,3]), (2))
        self.__add_test_case__("Test 2", (7, [2, 3, 1, 2, 4, 3,7]), (1))
        self.__add_test_case__("Test 3", (7, []), (0))
        self.__add_test_case__("Test 4", (3, [1, 1]), (0))