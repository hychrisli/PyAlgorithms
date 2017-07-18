from src.base.test_cases import TestCases
from src.mappers.list2treenode import to_binary_tree
from src.structures.treenode import TreeNode

class HouseRobberIIITestCases(TestCases):

    def __init__(self):
        super(HouseRobberIIITestCases, self).__init__()
        self.__add_test_case__("Example 1", self.__get_tree_one__(), 7)
        self.__add_test_case__("Example 2", self.__get_tree_two__(), 9)
        self.__add_test_case__("Test 3", self.__get_tree_three__(), 12)


    def __get_tree_one__(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        cur_node = root.left
        cur_node.right = TreeNode(3)

        cur_node = root.right
        cur_node.right = TreeNode(1)

        return root

    def __get_tree_two__(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)

        cur_node = root.left
        cur_node.left = TreeNode(1)
        cur_node.right = TreeNode(3)

        cur_node = root.right
        cur_node.right = TreeNode(1)

        return root


    def __get_tree_three__(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)

        cur_node = root.left
        cur_node.left = TreeNode(1)
        cur_node.right = TreeNode(4)

        cur_node = cur_node.left
        cur_node.right = TreeNode(2)

        return root