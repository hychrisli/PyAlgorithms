from src.base.test_cases import TestCases

class CombinationsTestCases(TestCases):
    def __init__(self):
        super(CombinationsTestCases, self).__init__()
        self.__add_test_case__('Test 1', (4, 2), [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]])