from src.base.test_cases import TestCases
from src.mappers.list2linkedlist import to_linkedlist

class RotateListTestCases(TestCases):

    def __init__(self):

        super(RotateListTestCases, self).__init__()
        self.__add_test_case__('Test 1', (to_linkedlist([1,2,3,4,5,6,7]), 2), to_linkedlist([6,7,1,2,3,4,5]))
        self.__add_test_case__('Test 2', (to_linkedlist([1, 2, 3, 4, 5, 6, 7]), 9),
                               to_linkedlist([6, 7, 1, 2, 3, 4, 5]))
        self.__add_test_case__('Test 2', (to_linkedlist([]), 0), to_linkedlist([]))