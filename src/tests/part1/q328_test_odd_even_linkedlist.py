from src.base.test_cases import TestCases
import src.mappers.list2linkedlist as l2l


class OddEvenLinkedlistTestCases(TestCases):

    def __init__(self):
        super(OddEvenLinkedlistTestCases, self).__init__()
        self.__add_test_case__("Test 1", l2l.to_linkedlist([1,2,3,4,5,6]), l2l.to_linkedlist([1,3,5,2,4,6]))