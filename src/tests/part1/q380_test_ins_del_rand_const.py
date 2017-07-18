from src.base.test_cases import TestCases
from src.utility.constants import INSERT, REMOVE, GET_RANDOM

class InsDelRandConstTestCases(TestCases):

    def __init__(self):
        super(InsDelRandConstTestCases, self).__init__()
        self.__add_test_case__('Test Insert 1', (INSERT, 1), True)
        self.__add_test_case__('Test Remove 2', (REMOVE, 2), False)
        self.__add_test_case__('Test Insert 2', (INSERT, 2), True)
        self.__add_test_case__('Test Random', (GET_RANDOM, [1,2]), True)
        self.__add_test_case__('Test Remove 1', (REMOVE, 1), True)
        self.__add_test_case__('Test Insert 2', (INSERT, 2), False)
        self.__add_test_case__('Test Random', (GET_RANDOM, [2]), True)
        self.__add_test_case__('Test Remove 0', (REMOVE, 0), False)
        self.__add_test_case__('Test Remove 0', (REMOVE, 0), False)
        self.__add_test_case__('Test Insert 0', (INSERT, 0), True)
        self.__add_test_case__('Test Random', (GET_RANDOM, [0,2]), True)
        self.__add_test_case__('Test Remove 0', (REMOVE, 0), True)
        self.__add_test_case__('Test Insert 0', (INSERT, 0), True)



