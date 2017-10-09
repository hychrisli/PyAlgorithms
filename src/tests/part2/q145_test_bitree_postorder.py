from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_complete_binary_tree


class BiTreePostOrderTestCases(TestCases):


    def __init__(self):
        super(BiTreePostOrderTestCases, self).__init__()
        self.__add_test_case__('Test 1', to_complete_binary_tree([1, None, 2, None, None, 3, None]), [3, 2, 1])
        self.__add_test_case__('Test 2', to_complete_binary_tree([1, 2, 3, 4, 5, None, 6]), [4, 5, 2, 6, 3, 1])
        self.__add_test_case__('Test 3', None, [])
