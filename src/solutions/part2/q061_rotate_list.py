from src.base.solution import Solution
from src.structures.listnode import ListNode
from src.tests.part2.q061_test_rotate_list import RotateListTestCases

class RotateList(Solution):
    def gen_test_cases(self):
        return RotateListTestCases()

    def verify_output(self, test_output, output):
        res1 = test_output.to_str() if test_output else None
        res2 = output.to_str() if output else None
        return res1 == res2

    def print_output(self, output):
        res = output.to_str() if output else None
        print(res)

    def run_test(self, input):
        return self.rotateRight(input[0], input[1])

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        hd = ListNode(None)
        hd.next, lpt, fpt = head, hd, hd
        cnt = k

        while cnt and lpt.next:
            lpt = lpt.next
            cnt -= 1

        # Handles case when k is greater than the length of the linkedlist
        if not lpt.next and cnt != k:

            n = k - cnt
            cnt = k % n
            lpt = hd
            for _ in xrange(cnt):
                lpt = lpt.next

        while lpt.next:
            lpt = lpt.next
            fpt = fpt.next

        lpt.next = hd.next
        hd.next = fpt.next
        fpt.next = None

        return hd.next

if __name__ == '__main__':

    sol = RotateList()
    sol.run_tests()