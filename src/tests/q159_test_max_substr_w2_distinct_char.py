from src.base.test_cases import TestCases

class MaxSubStrW2DistinctCharTestCases(TestCases):

    def __init__(self):
        super(MaxSubStrW2DistinctCharTestCases, self).__init__()
        self.__add_test_case__('Test 1', 'abcbbbbcccbdddadacb', 10)
        self.__add_test_case__('Test 2', 'abcbbbbcccdddadacb', 9)
        self.__add_test_case__('Test 3', 'abbbbbcccdddadacb', 8)
        self.__add_test_case__('Test 4', 'abbbcccdddadacb', 6)
        self.__add_test_case__('Test 5', 'abbcccdddadacb', 6)
        self.__add_test_case__('Test 6', 'abbcccddd', 6)