from src.base.test_cases import TestCases

class BuySellStockTestCases(TestCases):

    def __init__(self):
        super(BuySellStockTestCases, self).__init__()
        self.__add_test_case__('Test 1', [7, 1, 5, 3, 6, 4], 5)
        self.__add_test_case__('Test 2', [7, 6, 4, 3, 1], 0)
        self.__add_test_case__('Test 3', [], 0)