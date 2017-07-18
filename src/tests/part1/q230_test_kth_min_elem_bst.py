from src.base.test_cases import TestCases
import src.mappers.list2treenode as mapper

class KthMinElemBstTestCases(TestCases):
    def __init__(self):
        super(KthMinElemBstTestCases, self).__init__()
        self.__add_test_case__("Test 1", [self.get_bst_one(), 7], 8)

    @staticmethod
    def get_bst_one():
        tree_lst = [[6, 2, 8], [2, 0, 4], [4, 3, 5], [9, 8, 11]]
        return mapper.to_binary_tree(tree_lst)
