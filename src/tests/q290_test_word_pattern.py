from src.base.test_cases import TestCases
from src.base.test_case import TestCase


class WordPatternTestCases(TestCases):

    def __init__(self):
        super(WordPatternTestCases, self).__init__()
        self.__add_test_case__("example test 1", ("abba", "dog cat cat dog"), (True))
        self.__add_test_case__("test 2", ("abba", "dog cat cat fish"), (False))
        self.__add_test_case__("test 3", ("jquery", "jquery"), (False))
        self.__add_test_case__("test 4", ("abba", "dog dog dog dog"), (False))

