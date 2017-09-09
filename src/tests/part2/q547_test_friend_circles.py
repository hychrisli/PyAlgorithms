from src.base.test_cases import TestCases


class FriendCirclesTestCases(TestCases):
    def __init__(self):
        super(FriendCirclesTestCases, self).__init__()
        self.__add_test_case__('Test 1', [[1, 1, 0],
                                          [1, 1, 0],
                                          [0, 0, 1]], 2)
        self.__add_test_case__('Test 2', [[1, 1, 0],
                                          [1, 1, 1],
                                          [0, 1, 1]], 1)

        self.__add_test_case__('Test 3', [[1, 1, 0, 0, 1],
                                          [1, 1, 0, 0, 1],
                                          [0, 0, 1, 0, 0],
                                          [0, 0, 0, 1, 0],
                                          [1, 1, 0, 0, 1]], 3)


        self.__add_test_case__('Test 4', [[1, 1, 0, 1, 1, 0, 0],
                                          [1, 1, 0, 1, 0, 0, 1],
                                          [0, 0, 1, 0, 1, 1, 0],
                                          [1, 1, 0, 1, 1, 1, 1],
                                          [1, 0, 1, 1, 1, 0, 0],
                                          [0, 0, 1, 1, 0, 1, 1],
                                          [0, 1, 0, 1, 0, 1, 1]], 1)

