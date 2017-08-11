from src.base.solution import Solution
from src.tests.part2.q234_test_linked_palin import LinkedPalinTestCases
from src.structures.listnode import ListNode

class LinkedPalin(Solution):
    def gen_test_cases(self):
        return LinkedPalinTestCases()

    def run_test(self, input):
        return self.isPalindrome(input)

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast, slow = head, head
        nhead = ListNode(None)
        if not fast or not fast.next: return True

        while fast and fast.next:

            fast = fast.next.next

            tmp = slow
            slow = slow.next

            tmp.next = nhead.next
            nhead.next = tmp

        npt = nhead.next

        if not fast: opt = slow
        else: opt = slow.next

        while npt:
            if npt.val != opt.val:
                return False
            npt, opt = npt.next, opt.next


        return True

if __name__ == '__main__':
    sol = LinkedPalin()
    sol.run_tests()