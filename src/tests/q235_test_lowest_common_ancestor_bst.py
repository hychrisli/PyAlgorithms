from src.base.test_cases import TestCases
import src.mappers.list2treenode as mapper


class LowestCommonAncestorBstTestCases(TestCases):

    def __init__(self):
        super(LowestCommonAncestorBstTestCases, self).__init__()
        self.__add_test_case__("Test Example 1", [self.__get_tree_one__(), 2, 8], 6)

    @staticmethod
    def __get_tree_one__():
        tree_lst = [[6, 2, 8], [2, 0, 4], [4, 3, 5], [8, 7, 9]]
        return mapper.to_binary_tree(tree_lst)
#,