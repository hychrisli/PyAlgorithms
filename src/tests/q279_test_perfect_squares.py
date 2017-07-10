from src.base.test_cases import TestCases

class PerfectSquaresTestCases(TestCases):

    def __init__(self):
        super(PerfectSquaresTestCases, self).__init__()
        self.__add_test_case__("Example 1", 12, 3)
        self.__add_test_case__("Example 2", 13, 2)