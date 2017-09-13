from src.base.test_cases import TestCases


class SimplifiyPathTestCases(TestCases):

    def __init__(self):
        super(SimplifiyPathTestCases, self).__init__()
        self.__add_test_case__('Test 1', '/home/', '/home')
        self.__add_test_case__('Test 2', '/a/./b/../../c/', '/c')
        self.__add_test_case__('Test 3', '/../', '/')
        self.__add_test_case__('Test 4', '/home//foo/', '/home/foo')