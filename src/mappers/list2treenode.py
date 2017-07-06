from src.structures.treenode import TreeNode


def to_complete_binary_tree(lst):
    """
    Complete Binary Tree
    :param lst:
    :return:
    """

    llen = len(lst)
    if llen < 1: return None
    tree = [TreeNode(lst[0])]
    idx = 1

    while idx < llen:
        pidx = idx / 2
        tree.append(TreeNode(lst[idx]))
        if idx % 2 == 1:
            tree[pidx].left = tree[idx]
        else:
            tree[pidx].right = tree[idx]
        idx += 1

    print(tree)
    return tree[0]