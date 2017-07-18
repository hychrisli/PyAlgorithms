from src.base.solution import Solution
from src.tests.part2.q082_test_rm_duplicates_sorted_list_ii import RmDuplicatesSortedListIITestCases
from src.structures.listnode import ListNode

class RmDuplicatesSortedListII(Solution):
    def run_test(self, input):
        return self.deleteDuplicates(input)

    def verify_output(self, test_output, output):

        str1 = test_output.to_str() if test_output else None
        str2 = output.to_str() if output else None
        return str1 == str2

    def print_output(self, output):
        print(output.to_str() if output else None)

    def gen_test_cases(self):
        return RmDuplicatesSortedListIITestCases()

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fpt = h = ListNode(None)
        lpt = head.next if head else None
        stack = [head]

        while lpt:

            if lpt.val == stack[-1].val:
                stack.append(lpt)
            else:
                if len(stack) == 1:
                    fpt.next = stack.pop()
                    fpt = fpt.next
                else:
                    while stack:
                        stack.pop()
                stack.append(lpt)
            # print([x.val for x in stack])
            # print(h.to_str())
            lpt = lpt.next

        if len(stack) == 1:
            fpt.next = stack.pop()
        else:
            fpt.next = None

        return h.next

# 1->2->3->3->4->4->5
# lpt 3
# cpt 3
# lpt 1


if __name__ == '__main__':
    sol = RmDuplicatesSortedListII()
    sol.run_tests()
