from src.base.test_cases import TestCases
from src.base.test_case import TestCase


class WordPatternTestCases(TestCases):

    def __init__(self):
        super(WordPatternTestCases, self).__init__()
        self.__add_test_case__("example test 1", ["abba", "dog cat cat dog"], [True])

