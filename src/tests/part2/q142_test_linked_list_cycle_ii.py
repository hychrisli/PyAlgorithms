from src.base.test_cases import TestCases
from src.mappers.list2linkedlist import to_linkedlist

class LinkedListCycleIiTestCases(TestCases):

    def __init__(self):

        super(LinkedListCycleIiTestCases, self).__init__()
        head, begin = self.gen_list1()
        self.__add_test_case__('Test 1', head, begin)

        head, begin = self.gen_list2()
        self.__add_test_case__('Test 2', head, begin)


    @staticmethod
    def gen_list1():
        head = to_linkedlist([1, 2, 3, 4, 5, 6, 7])
        cur = head

        while cur.next:
            cur = cur.next

        cur.next = head.next.next

        return head, cur.next



    @staticmethod
    def gen_list2():
        head = to_linkedlist([1, 2, 3, 4, 5, 6])
        cur = head

        while cur.next:
            cur = cur.next

        cur.next = head.next
        return head, cur.next
