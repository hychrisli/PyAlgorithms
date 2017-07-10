

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


    def to_str(self):
        pt = self
        lstr = ""
        while pt:
            lstr += str(pt.val) + " -> "
            pt = pt.next

        return lstr