

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


    def to_str(self):
        root = self
        lstr = ""
        while root:
            lstr += root.val + " -> "

        return lstr