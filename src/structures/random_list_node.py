# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def to_str(self):
        return RandomListNode.random_to_str(self)

    @staticmethod
    def random_to_str(root):

        if root is None:
            return ""

        if root.random is None:
            return RandomListNode.random_to_str(root.next)
        else:
            return "[" + str(root.label) + "," + str(root.random.label) + "] " + RandomListNode.random_to_str(root.next)