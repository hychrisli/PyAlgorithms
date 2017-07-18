from src.base.test_cases import TestCases

class CipherTestCases(TestCases):

    def __init__(self):
        super(CipherTestCases, self).__init__()
        self.__add_test_case__('Test 1', [7,4,'1110100110'], '1001010')
        self.__add_test_case__('Test 2', [6, 2, '1110001'], '101111')