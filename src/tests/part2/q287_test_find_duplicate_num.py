from src.base.test_cases import TestCases

class FindDuplicateNumTestCases(TestCases):

    def __init__(self):
        super(FindDuplicateNumTestCases, self).__init__()
        self.__add_test_case__('Test 1', [3, 1 ,2, 2], 2)
        self.__add_test_case__('Test 2', [6, 2, 3, 4, 1, 8, 7, 9, 5, 10, 3],3)