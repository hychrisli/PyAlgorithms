from src.base.test_cases import TestCases

class MinPathSumTestCases(TestCases):

    def __init__(self):
        super(MinPathSumTestCases, self).__init__()
        self.__add_test_case__("Test 1", [[1,0,2,1],[1,2,0,1], [2,0,1,1],[1,2,0,1],[1,1,0,2],[1,1,0,1]], 5)