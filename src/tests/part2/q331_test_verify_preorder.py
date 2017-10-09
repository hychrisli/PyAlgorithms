from src.base.test_cases import TestCases


class VerifyPreOrderTestCases(TestCases):

    def __init__(self):
        super(VerifyPreOrderTestCases, self).__init__()
        self.__add_test_case__('Test 1',"9,3,4,#,#,1,#,#,2,#,6,#,#", True )
        self.__add_test_case__('Test 2', "1,#", False)
        self.__add_test_case__('Test 3', "9,#,#,1", False)
        self.__add_test_case__('Test 4', "#,#,1", False)
        self.__add_test_case__('Test 5', "5,#,1,2,3", False)
        self.__add_test_case__('Test 6', "#", True)
        self.__add_test_case__('Test 7', "9,9,#,#,9,#,#", True)
        self.__add_test_case__('Test 8', "9,3,4,#,#,1,#,#,#,2,#,6,#,#", False)
