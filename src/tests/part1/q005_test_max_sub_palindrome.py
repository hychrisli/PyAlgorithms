from src.base.test_cases import TestCases

class MaxSubPalindromeTestCases(TestCases):
    def __init__(self):
        super(MaxSubPalindromeTestCases, self).__init__()
        self.__add_test_case__("Test 1", "bababa", {"babab", "ababa"})
        self.__add_test_case__("Test 2", "bacaba", {"bacab"})
        self.__add_test_case__("Test 3", "bacacd", {"aca", "cac"})
        self.__add_test_case__("Test 4", "aaabaaaa", {"aaabaaa"})
        self.__add_test_case__("Test 5", "a", {"a"})