from src.base.test_cases import TestCases


class QueueOnStackTestCases(TestCases):
    def __init__(self):
        super(QueueOnStackTestCases, self).__init__()
        self.__add_test_case__("Test 1", ([1,2,3,4]), (1, 2, False))