from src.base.solution import Solution
from src.structures.listnode import ListNode
from src.tests.part1.q083_test_rm_duplicates_sorted_list import RmDuplicatesSortedListTestCases


class RmDuplicatesSortedList(Solution):
    def run_test(self, input):
        return self.deleteDuplicates(input)

    def gen_test_cases(self):
        return RmDuplicatesSortedListTestCases()

    def verify_output(self, test_output, output):
        return test_output.to_str() == output.to_str()

    def print_output(self, output):
        print(output.to_str())

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curval = None
        pre = ListNode(curval)
        pt = head

        while pt:
            if pt.val != curval:
                pre.next = pt
                pre = pt
                curval = pt.val
            pt = pt.next
        pre.next = None # handling the last point

        return head


if __name__ == '__main__':
    sol = RmDuplicatesSortedList()
    sol.run_tests()