from src.base.test_cases import TestCases

class ReversePolishNotationTestCases(TestCases):

    def __init__(self):
        super(ReversePolishNotationTestCases, self).__init__()
        self.__add_test_case__('Test 1', ["2", "1", "+", "3", "*"], 9)
        self.__add_test_case__('Test 2', ["4", "13", "5", "/", "+"], 6)
        self.__add_test_case__('Test 3', ["15"], 15)
        self.__add_test_case__('Test 4', ["10","126","9","3","+","-11","*","/","*","17","+","5","+"], 22)