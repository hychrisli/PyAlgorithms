from src.base.test_cases import TestCases

class ArrayProductTestCases(TestCases):

    def __init__(self):
        super(ArrayProductTestCases, self).__init__()
        self.__add_test_case__('Test 1', [1, 2, 3, 4], [24, 12, 8, 6])