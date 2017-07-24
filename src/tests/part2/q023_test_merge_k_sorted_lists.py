from src.base.test_cases import TestCases
from src.mappers.list2linkedlist import to_linkedlist


class MergeKSortedListsTestCases(TestCases):

    def __init__(self):
        super(MergeKSortedListsTestCases, self).__init__()
        self.__add_test_case__("Test 1", self.get_lists(), to_linkedlist([1, 2, 2, 3, 4, 5, 8, 9, 10, 12, 14]))
        self.__add_test_case__("Test 2", [], None)


    def get_lists(self):
        res = []
        res.append(to_linkedlist([2,2,3,4]))
        res.append(to_linkedlist([1,5,8,10]))
        res.append(to_linkedlist([9,12,14]))
        return res