from src.base.test_cases import TestCases


class PartParlindromeTestCases(TestCases):

    def __init__(self):
        super(PartParlindromeTestCases, self).__init__()
        self.__add_test_case__("Test 1", "aab", [["aa", "b"], ["a", "a", "b"]])
        self.__add_test_case__("Test 2", "a", [["a"]])
        self.__add_test_case__(
            "Test 3",
            "aabac",
            [
                ["a", "a", "b", "a", "c"],
                ["a", "aba", "c"],
                ["aa", "b", "a", "c"]
            ])
        self.__add_test_case__("Test 4", "", [[]])