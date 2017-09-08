from src.base.test_cases import TestCases

class IsSubSeqTestCases(TestCases):

    def __init__(self):

        super(IsSubSeqTestCases, self).__init__()
        self.__add_test_case__('Test 1', ('ace', 'abcde'), True)
        self.__add_test_case__('Test 2', ('aec', 'abcde'), False)
        self.__add_test_case__('Test 3', ('', 'abcags'), True)