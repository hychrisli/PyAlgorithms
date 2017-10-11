from src.base.test_cases import TestCases


class MajorElemIiTestCases(TestCases):

    def __init__(self):
        super(MajorElemIiTestCases,self).__init__()
        self.__add_test_case__('Test 1', [5, 0, 5, 0, 1, 0, 5], [5, 0])
        self.__add_test_case__('Test 2', [5, 0, 5, 0, 1, 5], [5])
        self.__add_test_case__('Test 3', [5, 0, 5, 0, 1, 1, 1, 5], [1, 5])
        self.__add_test_case__('Test 4', [2, 2], [2])
        self.__add_test_case__('Test 5', [0,-1,2,-1], [-1])
        self.__add_test_case__('Test 6', [0, 0, 0], [0])