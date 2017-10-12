from src.base.test_cases import TestCases

class RotatedSearchIiTestCases(TestCases):

    def __init__(self):
        super(RotatedSearchIiTestCases, self).__init__()
        self.__add_test_case__('Test 1', ([4,5,6,7,0,1,2], 5), True)
        self.__add_test_case__('Test 2', ([4, 5, 6, 7, 0, 1, 2], 1), True)
        self.__add_test_case__('Test 3', ([4, 5, 6, 7, 0, 1, 2], 2), True)
        self.__add_test_case__('Test 4', ([4, 5, 6, 7, 0, 1, 2], 0), True)
        self.__add_test_case__('Test 5', ([4, 5, 6, 7, 0, 1, 2], 4), True)
        self.__add_test_case__('Test 6', ([4, 5, 6, 7, 0, 1, 2], 6), True)
        self.__add_test_case__('Test 7', ([4, 5, 6, 7, 0, 1, 2, 4, 4, 4], 5), True)
        self.__add_test_case__('Test 7', ([4, 5, 6, 7, 0, 1, 2, 4, 4, 4], 3), False)
        self.__add_test_case__('Test 8', ([1, 1, 3, 1], 3), True)
        self.__add_test_case__('Test 9', ([1, 1, 1, 3, 1], 3), True)
        self.__add_test_case__('Test 10', ([1, 3, 1, 1, 1], 3), True)
        self.__add_test_case__('Test 11', ([1, 1, 3, 1], 2), False)
        self.__add_test_case__('Test 12', ([0, 0, 1, 1, 2, 0], 2), True)