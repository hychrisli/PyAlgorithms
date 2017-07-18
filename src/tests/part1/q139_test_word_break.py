from src.base.test_cases import TestCases


class WordBreakTestCases(TestCases):

    def __init__(self):
        super(WordBreakTestCases,self).__init__()
        self.__add_test_case__('Test 1', ("leetcode", ["leet", "code"]), True)
        self.__add_test_case__('Test 2', ("abacdd", ["aba", "cdd"]), True)
        self.__add_test_case__('Test 3', ("abacdd", ["cdc", "aba"]), False)
        self.__add_test_case__('Test 4', ("abacdd", []), False)
        self.__add_test_case__('Test 5', ("a", ["cd"]), False)