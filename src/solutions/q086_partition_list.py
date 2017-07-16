from src.base.solution import Solution
from src.tests.q086_test_partition_list import PartitionListTestCases
from src.structures.listnode import ListNode

class PartitionList(Solution):
    def gen_test_cases(self):
        return PartitionListTestCases()

    def run_test(self, input):
        return self.partition(input[0], input[1])

    def verify_output(self, test_output, output):
        return test_output.to_str() == output.to_str()

    def print_output(self, output):
        print(output.to_str())

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        lhead, ghead = ListNode(None), ListNode(None)
        lhead.next = head

        lpt, gpt = lhead, ghead

        while lpt.next:
            if lpt.next.val >= x:
                gpt.next = lpt.next
                lpt.next = lpt.next.next

                gpt = gpt.next
                gpt.next = None
            else:
                lpt = lpt.next

        lpt.next = ghead.next
        return lhead.next

# Test
# 1->4->3->2->5->2 and x = 3
# lpt = Node(2) -> Node(None)
# gpt = Node(5) -> Node(None)
# lhead = None->1->2->2
# ghead = None->4->3->5



if __name__ == '__main__':
    sol = PartitionList()
    sol.run_tests()