from src.base.test_cases import TestCases

class HammingDistTestCases(TestCases):

    def __init__(self):
        super(HammingDistTestCases, self).__init__()
        self.__add_test_case__('Test 1', (1, 4), 2)
        