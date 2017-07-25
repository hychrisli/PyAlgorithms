from src.base.test_cases import TestCases

class WiggleSortIiTestCases(TestCases):

    def __init__(self):
        super(WiggleSortIiTestCases,self).__init__()
        self.__add_test_case__('Test 1', [1, 5, 1, 1, 6, 4], [1, 4, 1, 5, 1, 6])
        self.__add_test_case__('Test 2', [1, 3, 2, 2, 3, 1], [2, 3, 1, 3, 1, 2])
        self.__add_test_case__('Test 3', [1,1,2,1,2,2,1], [1, 2, 1, 2, 1, 2, 1])
        self.__add_test_case__('Test 4', [4,5,5,6], [5,6,4,5])