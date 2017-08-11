from src.base.test_cases import TestCases
from src.mappers.list2linkedlist import to_linkedlist

class LinkedPalinTestCases(TestCases):

    def __init__(self):
        super(LinkedPalinTestCases, self).__init__()
        self.__add_test_case__('Test 1', to_linkedlist(['a', 'a', 'b', 'a', 'a']), True)
        self.__add_test_case__('Test 2', to_linkedlist(['a', 'a', 'b', 'b', 'a', 'a']), True)
        self.__add_test_case__('Test 3', to_linkedlist(['a', 'a', 'b', 'a', 'c']), False)
        self.__add_test_case__('Test 4', to_linkedlist(['a', 'a', 'b']), False)
        self.__add_test_case__('Test 4', to_linkedlist(['a', 'a']), True)
        self.__add_test_case__('Test 4', to_linkedlist(['a']), True)
        self.__add_test_case__('Test 4', to_linkedlist([]), True)