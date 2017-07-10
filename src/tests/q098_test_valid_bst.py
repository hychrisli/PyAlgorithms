from src.base.test_cases import TestCases
from src.structures.treenode import TreeNode

class ValidBstTestCases(TestCases):
    def __init__(self):
        super(ValidBstTestCases, self).__init__()
        self.__add_test_case__("Test1", self.__get_first_tree__(), False)
        self.__add_test_case__("Test1", self.__get_tree_two__(), True)



    def __get_first_tree__(self):
        root = TreeNode(6)
        root.left = TreeNode(4)
        root.right = TreeNode(7)

        cur_node = root.left
        cur_node.left = TreeNode(1)
        cur_node.right = TreeNode(3)

        cur_node = cur_node.right
        cur_node.left = TreeNode(2)

        return root

    def __get_tree_two__(self):
        root = TreeNode(6)
        root.left = TreeNode(4)
        root.right = TreeNode(7)

        cur_node = root.left
        cur_node.left = TreeNode(1)
        cur_node.right = TreeNode(5)

        cur_node = root.right
        cur_node.right = TreeNode(9)

        return root





