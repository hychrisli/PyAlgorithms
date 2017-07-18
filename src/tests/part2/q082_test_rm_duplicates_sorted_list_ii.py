from src.base.test_cases import TestCases
from src.mappers.list2linkedlist import to_linkedlist


class RmDuplicatesSortedListIITestCases(TestCases):
    def __init__(self):
        super(RmDuplicatesSortedListIITestCases, self).__init__()
        self.__add_test_case__('Test 1', to_linkedlist([1,2,3,3,4,4,5]), to_linkedlist([1,2,5]))
        self.__add_test_case__('Test 2', to_linkedlist([1,1,1,2,2,3]), to_linkedlist([3]))
        self.__add_test_case__('Test 3', to_linkedlist([]), to_linkedlist([]))