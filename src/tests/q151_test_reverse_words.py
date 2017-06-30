from src.base.test_cases import TestCases

class ReverseWordsTestCases(TestCases):
    def __init__(self):
        super(ReverseWordsTestCases, self).__init__()
        self.__add_test_case__("Example Test 1", ("the sky is blue"), ("blue is sky the"))
        self.__add_test_case__("Test 2", (" "), (""))
        self.__add_test_case__("Test 3", ("   a   b "), ("b a"))
        self.__add_test_case__("Test 4", ("  a  "), ("a"))
        self.__add_test_case__("Test 5", (""), (""))
        self.__add_test_case__("Test 6", (" 1"), ("1"))
