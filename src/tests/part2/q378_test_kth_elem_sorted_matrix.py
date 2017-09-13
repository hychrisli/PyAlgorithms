from src.base.test_cases import TestCases

class KthElemSortedMatrixTestCases(TestCases):

    def __init__(self):
        super(KthElemSortedMatrixTestCases, self).__init__()
        self.__add_test_case__('test 1', ([[1,5,9],[10,11,13],[12,13,15]], 8), 13)
        self.__add_test_case__('test 2', ([[1, 5, 9], [10, 11, 13], [11, 12, 15]], 6), 11)
        self.__add_test_case__('test 3', ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 1), 1)
        self.__add_test_case__('test 4', ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 4), 10)