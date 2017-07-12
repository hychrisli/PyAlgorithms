from src.base.test_cases import TestCases


class WordBreakTestCases(TestCases):
    def __ini__(self):
        super(WordBreakTestCases,self).__init__()
        self.__add_test_case__('Test 1', ("leetcode", ["leet", "code"]), True)