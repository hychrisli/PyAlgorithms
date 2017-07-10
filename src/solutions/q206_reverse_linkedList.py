from src.base.solution import Solution
from src.tests.q206_test_reverse_linkedlist import ReverseLinkedListTestCases
from src.structures.listnode import ListNode

class ReverseLinkedList(Solution):
    def run_test(self, input):
        return self.reverseList(input)

    def print_output(self, output):
        print(output.to_str())

    def verify_output(self, test_output, output):
        return output.to_str() == test_output.to_str()

    def gen_test_cases(self):
        return ReverseLinkedListTestCases()

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pt = head
        rhead = ListNode(None)

        while pt:
            tmp = rhead.next
            rhead.next = pt

            pt = pt.next
            rhead.next.next = tmp

        return rhead.next



if __name__ == '__main__':
    sol = ReverseLinkedList()
    sol.run_tests()