from src.base.test_cases import TestCases


class FindDiffTestCases(TestCases):
    def __init__(self):
        super(FindDiffTestCases, self).__init__()
        self.__add_test_case__("Example 1", ("abcd", "abced"), ('e'))