from src.base.test_cases import TestCases

class UglyNumTestCases(TestCases):

    def __init__(self):
        super(UglyNumTestCases, self).__init__()
        self.__add_test_case__('Test 1', 10, 12)
        self.__add_test_case__('Test 2', 20, 36)