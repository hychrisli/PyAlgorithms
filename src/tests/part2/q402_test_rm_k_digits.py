from src.base.test_cases import TestCases

class RmKDigitsTestCases(TestCases):

    def __init__(self):

        super(RmKDigitsTestCases, self).__init__()
        self.__add_test_case__('Test 1', ('1432219',3), '1219')
        self.__add_test_case__('Test 2', ('10200', 1), '200')
        self.__add_test_case__('Test 3', ('12341382308123012390345032454756', 10), '123012390345032454756')
        self.__add_test_case__('Test 4', ('10', 2), '0')