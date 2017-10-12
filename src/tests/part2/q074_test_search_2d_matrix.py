from src.base.test_cases import TestCases


class Search2dMatrixTestCases(TestCases):
    def __init__(self):
        super(Search2dMatrixTestCases, self).__init__()
        self.__add_test_case__("Test 1",
                               ([
                                    [1, 3, 5, 7],
                                    [10, 11, 16, 20],
                                    [23, 30, 34, 50]
                                ], 3), True)

        self.__add_test_case__("Test 2",
                               ([
                                    [1, 3, 5, 7],
                                    [10, 11, 16, 20],
                                    [23, 30, 34, 50]
                                ], 24), False)
        self.__add_test_case__("Test 3",
                               ([
                                    [1, 3, 5, 7],
                                    [10, 11, 16, 20],
                                    [23, 30, 34, 50]
                                ], 7), True)

        self.__add_test_case__("Test 4",
                               ([
                                    [1, 3, 5, 7],
                                    [10, 11, 16, 20],
                                    [23, 30, 34, 50]
                                ], 8), False)

        self.__add_test_case__("Test 5",
                               ([
                                    [1, 3, 5, 7],
                                    [10, 11, 16, 20],
                                    [23, 30, 34, 50]
                                ], 0), False)
        self.__add_test_case__("Test 6",
                               ([], 0), False)

        self.__add_test_case__("Test 7",
                               ([[1], [3]], 3), True)




