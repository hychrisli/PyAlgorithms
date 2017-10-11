from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_complete_binary_tree

class ConstructBiTreeInPostOrderTestCases(TestCases):

    def __init__(self):
        super(ConstructBiTreeInPostOrderTestCases, self).__init__()
        self.__add_test_case__(
            'test 1',
            ([1, 2, 3, 4, 5, 8, 9], [2, 1, 4, 3, 9, 8, 5]),
            to_complete_binary_tree([5, 3, 8, 1, 4, None, 9, None, 2]))

        self.__add_test_case__(
            'test 2',
            ([-1], [-1]),
            to_complete_binary_tree([-1]))
        self.__add_test_case__(
            'test 3',
            ([1,3,2], [3, 2, 1]),
            to_complete_binary_tree([1, None, 2, None, None, 3]))