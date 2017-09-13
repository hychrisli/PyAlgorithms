from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_complete_binary_tree

class BitreeInorderTestCases(TestCases):

    def __init__(self):

        super(BitreeInorderTestCases, self).__init__()
        self.__add_test_case__('Test 1', to_complete_binary_tree([1, None, 2, None, None, 3, None]), [1,3,2])
        self.__add_test_case__('Test 2', to_complete_binary_tree([1, 2, 3, 4, 5, None, 6]), [4, 2, 5, 1, 3, 6])
        self.__add_test_case__('Test 3', None,[])