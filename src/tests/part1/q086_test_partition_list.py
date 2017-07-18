from src.base.test_cases import TestCases
from src.mappers.list2linkedlist import to_linkedlist

class PartitionListTestCases(TestCases):

    def __init__(self):
        super(PartitionListTestCases, self).__init__()
        self.__add_test_case__('Test 1', (to_linkedlist([1,4,3,2,5,2]), 3), (to_linkedlist([1,2,2,4,3,5])))