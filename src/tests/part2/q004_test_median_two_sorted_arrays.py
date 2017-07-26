from src.base.test_cases import TestCases

class MedianTwoSortedArraysTestCases(TestCases):

    def __init__(self):
        super(MedianTwoSortedArraysTestCases, self).__init__()
        self.__add_test_case__('Test 1', ([1, 4, 6, 9], [2, 3, 7, 8]), 5)
        self.__add_test_case__('Test 2', ([1, 2, 3, 4], [5, 6, 7]), 4)
        self.__add_test_case__('Test 3', ([1], [2]), 1.5)
        self.__add_test_case__('Test 4', ([1], [2,3]), 2)