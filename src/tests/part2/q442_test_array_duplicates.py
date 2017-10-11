from src.base.test_cases import TestCases


class ArrayDuplicatesTestCases(TestCases):

    def __init__(self):
        super(ArrayDuplicatesTestCases, self).__init__()
        self.__add_test_case__('Test 1', [4,3,2,7,8,2,3,1], [2, 3])