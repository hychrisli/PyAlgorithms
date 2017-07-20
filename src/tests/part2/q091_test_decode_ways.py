from src.base.test_cases import TestCases

class DecodeWaysTestCases(TestCases):

    def __init__(self):
        super(DecodeWaysTestCases, self).__init__()
        self.__add_test_case__('Test 1', "122324", 10)
        self.__add_test_case__('Test 2', "122304", 0)
        self.__add_test_case__('Test 3', "1220412", 4)
        self.__add_test_case__('Test 4', "", 0)