from src.base.test_cases import TestCases

class MaxSubPalindromeTestCases(TestCases):
    def __init__(self):
        super(MaxSubPalindromeTestCases, self).__init__()
        self.__add_test_case__("Test 1", "bababa", "aba")