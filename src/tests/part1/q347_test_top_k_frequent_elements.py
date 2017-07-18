from src.base.test_cases import TestCases


class TopKFreqElemTestCases(TestCases):

    def __init__(self):
        super(TopKFreqElemTestCases, self).__init__()
        self.__add_test_case__("Example Test 1", ([1,1,1,2,2,3], 2), ([1,2]))
        self.__add_test_case__("Test 2", ([2,2,3,4,2,3,3,1,1,5,5,7], 3), ([3,2,5,1]))
        self.__add_test_case__("Test 3", ([1], 1), ([1]))
        self.__add_test_case__("Test 4", ([-1, -1], 1), ([-1]))