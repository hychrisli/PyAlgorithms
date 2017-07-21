from src.base.test_cases import TestCases


class IslandNumTestCases(TestCases):

    def __init__(self):
        super(IslandNumTestCases, self).__init__()
        self.__add_test_case__('Test1', ["11110","11010","11000","00000"], 1)