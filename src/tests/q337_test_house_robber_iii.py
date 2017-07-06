from src.base.test_cases import TestCases

from src.mappers.list2treenode import to_complete_binary_tree

class HouseRobberIIITestCases(TestCases):

    def __init__(self):
        super(HouseRobberIIITestCases, self).__init__()
        tree = to_complete_binary_tree([1, 2, 3, None, 5])
        print(tree.to_str())
        # self.__add_test_case__("Example 1")



if __name__ == '__main__':
    test = HouseRobberIIITestCases()