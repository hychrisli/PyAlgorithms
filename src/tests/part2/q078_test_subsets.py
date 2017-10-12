from src.base.test_cases import TestCases


class SubsetsTestCases(TestCases):

    def __init__(self):
        super(SubsetsTestCases, self).__init__()
        self.__add_test_case__("Test 1", [1, 2], [[], [1], [2], [1,2]])