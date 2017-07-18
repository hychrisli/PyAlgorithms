from src.base.test_cases import TestCases
import src.mappers.list2treenode as l2t


class PartSumIITestCases(TestCases):
    def __init__(self):
        super(PartSumIITestCases, self).__init__()
        self.__add_test_case__("Test 1", (self.__get_tree_one__(), 22),[[5, 4, 11, 2], [5,8,4,5]])

    def __get_tree_one__(self):
        input = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
        return l2t.to_complete_binary_tree(input)
