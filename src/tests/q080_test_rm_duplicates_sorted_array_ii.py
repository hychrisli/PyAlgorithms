from src.base.test_cases import TestCases

class RmDuplicatesSortedArrayIITestCases(TestCases):

    def __init__(self):
        super(RmDuplicatesSortedArrayIITestCases, self).__init__()
        self.__add_test_case__('Test 1', [1,1,1,2,2,3], 5)
        self.__add_test_case__('Test 1', [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4], 8)