from src.base.test_cases import TestCases

class MajorElemTestCases(TestCases):

    def __init__(self):
        super(MajorElemTestCases, self).__init__()
        self.__add_test_case__('Test 1', [5, 0, 5, 0, 5], 5)
        self.__add_test_case__('Test 2', [5, 5, 1, 5], 5)
        self.__add_test_case__('Test 4', [2, 2], 2)
        self.__add_test_case__('Test 6', [0, 0, 0], 0)