from src.base.test_cases import TestCases

class StackOnQueueTestCases(TestCases):
    def __init__(self):
        super(StackOnQueueTestCases, self).__init__()
        self.__add_test_case__('Test 1', ([1,2,3,4]), (4, 3, False))