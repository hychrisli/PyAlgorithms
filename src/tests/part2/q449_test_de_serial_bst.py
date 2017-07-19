from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_complete_binary_tree


class DeSerialBstTestCases(TestCases):

    def __init__(self):
        super(DeSerialBstTestCases, self).__init__()
        tree = to_complete_binary_tree([5, 3, 8,1,4,None,9,None,2])
        data = '5 3 1 n 2 n n 4 n n 8 n 9 n n'

        self.__add_test_case__( 'test 1', (tree, data), (data, tree))


