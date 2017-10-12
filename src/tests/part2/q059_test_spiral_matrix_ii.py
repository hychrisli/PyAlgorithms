from src.base.test_cases import TestCases


class SpiralMatrixIiTestCases(TestCases):
    def __init__(self):
        super(SpiralMatrixIiTestCases, self).__init__()
        self.__add_test_case__("Test 1", 3,
                               [
                                   [1, 2, 3],
                                   [8, 9, 4],
                                   [7, 6, 5]
                               ])
