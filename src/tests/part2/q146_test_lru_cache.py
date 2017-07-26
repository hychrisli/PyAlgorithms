from src.base.test_cases import TestCases

class LruCacheTestCases(TestCases):

    def __init__(self):
        super(LruCacheTestCases, self).__init__()
        self.__add_test_case__('Test 1', [], True)