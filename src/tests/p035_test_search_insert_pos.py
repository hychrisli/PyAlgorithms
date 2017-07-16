from src.base.test_cases import TestCases


class SearchInsertPosTestCases(TestCases):

    def __init__(self):
        super(SearchInsertPosTestCases, self).__init__()
        self.__add_test_case__('Test 1', ([1,3,5,6], 5), 2)
        self.__add_test_case__('Test 2', ([1,3,5,6], 4), 2)
        self.__add_test_case__('Test 3', ([1,3,5,6], 0), 0)
        self.__add_test_case__('Test 4', ([1,3,5,6], 7), 4)