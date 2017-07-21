from src.base.test_cases import TestCases


class RepeatDnaSeqTestCases(TestCases):

    def __init__(self):
        super(RepeatDnaSeqTestCases, self).__init__()
        self.__add_test_case__('Test1', "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"])
        self.__add_test_case__('Test2', "CCCCCCCCCC", [])
        self.__add_test_case__('Test3', "CCCCCCCCCCC", ["CCCCCCCCCC"])