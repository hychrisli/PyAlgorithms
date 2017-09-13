from src.base.solution import Solution
from src.tests.part2.q142_test_linked_list_cycle_ii import LinkedListCycleIiTestCases

class LinkedListCycleII(Solution):
    def gen_test_cases(self):
        return LinkedListCycleIiTestCases()

    def run_test(self, input):
        return self.detectCycle(input)

    def print_output(self, output):
        print(output.val)

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return None

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: break

        if slow != fast: return None

        # print(slow.val, fast.val)
        slow = head
        # print(slow.val, fast.val)

        while fast != slow:
            slow = slow.next
            fast = fast.next
            # print(fast.val, slow.val)

        return fast


if __name__ == '__main__':
    sol = LinkedListCycleII()
    sol.run_tests()