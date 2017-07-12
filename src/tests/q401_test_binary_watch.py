from src.base.test_cases import TestCases


class BinaryWatchTestCases(TestCases):
    def __init__(self):
        super(BinaryWatchTestCases, self).__init__()
        self.__add_test_case__('Test 1', 1, ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"])