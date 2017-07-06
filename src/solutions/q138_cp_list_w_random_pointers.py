from src.base.solution import Solution
from src.tests.q138_test_cp_list_w_random_pointers import CpListWRandomPointersTestCases
from src.structures.random_list_node import RandomListNode

"""
https://leetcode.com/problems/copy-list-with-random-pointer/#/description

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

class CpListWRandomPointers(Solution):
    def print_output(self, output):
        res = output.to_str() if output else ""
        print(res)

    def gen_test_cases(self):
        return CpListWRandomPointersTestCases()

    def verify_output(self, test_output, output):
        res1 = test_output.to_str() if test_output else ""
        res2 = output.to_str() if output else ""
        return  res1 == res2

    def run_test(self, input):
        return self.copyRandomList(input)

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        # Building a linked list by inserting new nodes

        ap = head
        while ap is not None:
            # print(ap.label)
            a2p = RandomListNode(ap.label)
            a2p.next = ap.next
            ap.next = a2p
            ap = a2p.next
            #print(ap.label)

        # print(head.to_str())

        # Connecting the random pointers
        bp = head
        while bp:
            if bp.random:
                bp.next.random = bp.random.next

            # Boundary condition
            # bp is always on the original nodes
            bp = bp.next.next

        # print(head.to_str())
        # Separate two linked list
        cp = head
        nhead = head.next if head else None
        ncp = nhead
        while ncp:
            cp.next = ncp.next
            cp = cp.next

            if cp:
                ncp.next = cp.next
            ncp = ncp.next

        return nhead


if __name__ == '__main__':
    sol = CpListWRandomPointers()
    sol.run_tests()