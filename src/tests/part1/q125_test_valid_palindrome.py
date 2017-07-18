from src.base.test_cases import TestCases


class ValidPalindromeTestCases(TestCases):
    def __init__(self):
        super(ValidPalindromeTestCases,self).__init__()
        self.__add_test_case__("Example 1", ("A man, a plan, a canal: Panama"), True)
        self.__add_test_case__("Example 2", ("race a car"), False)
        self.__add_test_case__("Example 3", (""), True)
        self.__add_test_case__("Test 4", ("ab;cd[]9[]sds(9d++cba"), True)
        self.__add_test_case__("Test 4", ("ab;cd[]9[]sds(95++cba"), False)
