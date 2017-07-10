from src.base.solution import Solution
from src.tests.q328_test_odd_even_linkedlist import OddEvenLinkedlistTestCases
from src.structures.listnode import ListNode


class OddEvenLinkedlist(Solution):
    def run_test(self, input):
        return self.oddEvenList(input)

    def gen_test_cases(self):
        return OddEvenLinkedlistTestCases()

    def verify_output(self, test_output, output):
        return test_output.to_str() == output.to_str()

    def print_output(self, output):
        print(output.to_str())

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        olst = elst = ehead = ListNode(None)
        olst_end = olst
        is_odd = True
        pt = head

        while pt:
            print (olst.to_str())
            print (elst.to_str())

            if is_odd:
                olst.next = pt
                olst = olst.next
                olst_end = olst
                is_odd = False
            else:
                elst.next = pt
                elst = elst.next
                is_odd = True
            pt = pt.next

        elst.next = None
        # print (olst.to_str())
        # print (elst.to_str())

        olst_end.next = ehead.next
        return head

if __name__ == '__main__':
    sol = OddEvenLinkedlist()
    sol.run_tests()