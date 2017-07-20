from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_complete_binary_tree

class ConstructBiTreePreInOrderTestCases(TestCases):

    def __init__(self):
        super(ConstructBiTreePreInOrderTestCases, self).__init__()
        self.__add_test_case__(
            'test 1',
            ([5, 3,1,2,4,8,9], [1,2,3,4,5,8,9]),
            to_complete_binary_tree([5,3,8,1,4,None,9,None,2]))

        self.__add_test_case__(
            'test 2',
            ([-1], [-1]),
            to_complete_binary_tree([-1]))