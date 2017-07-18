from src.base.test_cases import TestCases


class MinWinSubStrTestCases(TestCases):

    def __init__(self):
        super(MinWinSubStrTestCases, self).__init__()
        self.__add_test_case__('Test 1', ('ADOBECODEBANC', 'ABC'), 'BANC')
        self.__add_test_case__('Test 2', ('a', 'aa'), '')
        self.__add_test_case__('Test 3', ("aaaaaaaaaaaabbbbbcdd", "abcdd"), "abbbbbcdd")

