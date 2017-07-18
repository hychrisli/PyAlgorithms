from src.base.test_cases import TestCases
import src.mappers.list2linkedlist as l2l

class RmDuplicatesSortedListTestCases(TestCases):
    def __init__(self):
        super(RmDuplicatesSortedListTestCases, self).__init__()
        self.__add_test_case__("Test 1", l2l.to_linkedlist([1,1,2]), l2l.to_linkedlist([1,2]))
        self.__add_test_case__("Test 2", l2l.to_linkedlist([1,1,2,3,3]), l2l.to_linkedlist([1,2,3]))