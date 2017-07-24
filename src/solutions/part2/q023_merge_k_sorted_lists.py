from src.base.solution import Solution
from src.tests.part2.q023_test_merge_k_sorted_lists import MergeKSortedListsTestCases
from src.structures.listnode import ListNode

class MergeKSortedLists(Solution):
    def gen_test_cases(self):
        return MergeKSortedListsTestCases()

    def run_test(self, input):
        return self.mergeKLists(input)

    def print_output(self, output):
        print(output.to_str() if output else [])

    def verify_output(self, test_output, output):
        res1 = output.to_str() if test_output else []
        res2 = output.to_str() if output else []
        return res1 == res2

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        import heapq
        hq, head  = [], ListNode(None)

        for node in lists:
            if node:
                heapq.heappush(hq, (node.val, node))

        pt = head
        while hq:
            pt.next = heapq.heappop(hq)[1]
            pt = pt.next
            if pt.next:
                heapq.heappush(hq,(pt.next.val, pt.next))

        return head.next



    def mergeKLists_v1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.lsts = lists
        if lists: return self.merge_sort(0, len(lists) - 1)

    def merge_sort(self, i, j):

        if i < j:
            mid = (i + j) / 2
            left = self.merge_sort(i, mid)
            right = self.merge_sort(mid + 1, j)
            res = self.merge(left, right)
            # print(res.to_str() if res else None)
            return res

        return self.lsts[i]

    def merge(self,left, right):

        head = ListNode(None)
        pt = head

        while left and right:
            if left.val > right.val:
                pt.next = right
                right = right.next
            else:
                pt.next = left
                left = left.next
            pt = pt.next

        if left: pt.next = left
        if right: pt.next = right

        return head.next


if __name__ == '__main__':
    sol = MergeKSortedLists()
    sol.run_tests()

