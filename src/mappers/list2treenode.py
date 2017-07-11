from src.structures.treenode import TreeNode
import math

def to_complete_binary_tree(lst):
    """
    Complete Binary Tree
    :param lst: a list of tree nodes
    :return:
    """
    n = len(lst)
    if n < 1: return None
    tree = [TreeNode(lst[0])]

    for i in xrange(1,n):

        pidx = int(math.floor((i-1) / 2))
        tree.append(TreeNode(lst[i]))

        if tree[pidx].val == None or lst[i] == None:
            continue

        if i % 2 == 1:
            tree[pidx].left = tree[i]
        else:
            tree[pidx].right = tree[i]

    return tree[0]

def to_binary_tree_distinct_vals(lst):
    """
    To build a binary tree
    :param lst: list of list
    [[root, left, right], [root, left, right]]
    :return: head
    """

    tree_dict = dict() # val : TreeNode(val)
    for node in lst:
        tree_dict[node[0]] = tree_dict.get(node[0], TreeNode(node[0]))
        left_child = None
        if node[1] is not None:
            tree_dict[node[1]] = tree_dict.get(node[1], TreeNode(node[1]))
            left_child = tree_dict[node[1]]

        right_child = None
        if node[2] is not None:
            tree_dict[node[2]] = tree_dict.get(node[2], TreeNode(node[2]))
            right_child = tree_dict[node[2]]

        tree_dict[node[0]].left = left_child
        tree_dict[node[0]].right = right_child


    return tree_dict[lst[0][0]]
