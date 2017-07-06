from src.base.test_cases import TestCases

class PartEqualSubSumTestCases(TestCases):

    def __init__(self):
        super(PartEqualSubSumTestCases, self).__init__()
        self.__add_test_case__("Example 1", ([1, 5, 11, 5]), (True))
        self.__add_test_case__("Example 2", ([1, 2, 3, 5]), (False))