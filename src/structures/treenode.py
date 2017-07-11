# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def to_str(self, prefix, is_tail):

        res = prefix +  ('└── ' if is_tail else "├── ") + str(self.val) + "\n"

        if self.left:
            res += self.left.to_str(prefix + ("    " if is_tail else "│   "), False)
        elif self.right:
            res += prefix + ("    " if is_tail else "│   ") + "├── L(None)\n"
        # print("Left: \n" + res)

        if self.right:
            res += self.right.to_str(prefix + ("    " if is_tail else "│   "), True)
        elif self.left:
            res += prefix + ("    " if is_tail else "│   ") + "└── R(None)\n"
        # print("Right: \n" + res)

        return res

    def get_tree_str(self):
        return self.to_str("", False)