from src.base.test_cases import TestCases

class MinHeightTreesTestCases(TestCases):

    def __init__(self):
        super(MinHeightTreesTestCases, self).__init__()
        self.__add_test_case__("Test 1", (4, [[1, 0], [1, 2], [1, 3]]), [1])
        self.__add_test_case__("Test 2", (6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]), [3, 4])
        self.__add_test_case__("Test 3", (1, []), [0])