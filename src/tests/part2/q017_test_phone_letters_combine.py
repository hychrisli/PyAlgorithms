from src.base.test_cases import TestCases

class PhoneLettersCombineTestCases(TestCases):

    def __init__(self):
        super(PhoneLettersCombineTestCases, self).__init__()
        self.__add_test_case__('Test 1', "23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])