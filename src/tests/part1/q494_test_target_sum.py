from src.base.test_cases import TestCases


class TargetSumTestCases(TestCases):

    def __init__(self):
        super(TargetSumTestCases, self).__init__()
        self.__add_test_case__("Example 1", ([1, 1, 1, 1, 1], 3), (5))
        self.__add_test_case__("Example 2", ([1, 1, 2, 1, 1], 4), (4))



