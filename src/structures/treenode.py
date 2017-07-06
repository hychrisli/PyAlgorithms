# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def to_str(self, prefix, is_tail):

        res = prefix +  '└── ' if is_tail else "├── " + str(self.val) + "\n"

        if self.left is not None:
            res += self.left.to_str(prefix + "    " if is_tail else "│   ", False)
        elif self.right is not None:
            res += prefix + "    " if is_tail else "│   " + "├── L(null)\n"

        if self.right is not None:
            res += self.right.to_str(prefix + "    " if is_tail else "│   ", True)
        elif self.left is not None:
            res += prefix + "    " if is_tail else "│   " + "├── R(null)\n"

        return res

q = Queue()