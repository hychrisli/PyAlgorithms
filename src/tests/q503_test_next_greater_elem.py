from src.base.test_cases import TestCases

class NextGreaterElemTestCases(TestCases):

    def __init__(self):
        super(NextGreaterElemTestCases, self).__init__()
        self.__add_test_case__('Test 1', [1,2,1], [2, -1, 2])
        self.__add_test_case__('Test 2', [7, 6, 4, 2, 1, 3, 5], [-1, 7, 5, 3, 3,5, 7])
        self.__add_test_case__('Test 3', [1,1,1,1,1], [-1,-1,-1,-1,-1])