from src.base.test_cases import TestCases


class IslandNumTestCases(TestCases):

    def __init__(self):
        super(IslandNumTestCases, self).__init__()
        self.__add_test_case__('Test1', ["11110","11010","11000","00000"], 1)
        self.__add_test_case__('Test2', ["11000", "11000", "00100", "00011"], 3)
        self.__add_test_case__('Test3', [], 0)
        self.__add_test_case__('Test4', ["111","010","111"], 1)
        self.__add_test_case__('Test5', ["111","101", "111"], 1)