from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_complete_binary_tree


class BstIterTestCases(TestCases):


    def __init__(self):
        super(BstIterTestCases, self).__init__()
        self.__add_test_case__('Test 1', to_complete_binary_tree([5, 2, 6, 1, 3, None, 7]), [1, 2, 3, 5, 6, 7])
        self.__add_test_case__('Test 2', to_complete_binary_tree([3, 1, 4, None, 2]), [1, 2, 3, 4])
        self.__add_test_case__('Test 3', None, [])
