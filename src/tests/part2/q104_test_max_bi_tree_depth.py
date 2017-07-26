from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_complete_binary_tree

class MaxBiTreeDepthTestCases(TestCases):

    def __init__(self):
        super(MaxBiTreeDepthTestCases, self).__init__()
        self.__add_test_case__(
            "Test 1",
            to_complete_binary_tree([1, 2, 3, 4, 5, None, 7, 8]), 4)

        self.__add_test_case__(
            "Test 2",
            to_complete_binary_tree([1, 2, 3]), 2)