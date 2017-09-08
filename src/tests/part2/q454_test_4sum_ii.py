from src.base.test_cases import TestCases

class FourSumIiTestCases(TestCases):

    def __init__(self):
        super(FourSumIiTestCases, self).__init__()
        self.__add_test_case__('Test 1', ([1, 2], [-2, -1], [-1, 2], [0, 2]), 2)
        self.__add_test_case__('Test 1', ([1, 2, 1], [-2, -1, 0], [-1, 2, 0], [0, 2, -1]), 14)