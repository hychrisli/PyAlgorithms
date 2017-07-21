from src.base.test_cases import TestCases

class UniqueBstTestCases(TestCases):

    def __init__(self):
        super(UniqueBstTestCases, self).__init__()
        self.__add_test_case__('Test 1', 3, 5)
        self.__add_test_case__('Test 2', 4, 14)
        self.__add_test_case__('Test 3', 10, 16796)
        self.__add_test_case__('Test 4', 2, 2)
        self.__add_test_case__('Test 5', 1, 1)