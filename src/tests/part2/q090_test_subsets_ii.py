from src.base.test_cases import TestCases


class SubsetsIiTestCases(TestCases):
    def __init__(self):
        super(SubsetsIiTestCases, self).__init__()
        self.__add_test_case__("Test 1",
                               [1, 2, 2],
                               [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])
        self.__add_test_case__("Test 2",
                               [0],
                               [[], [0]])
        self.__add_test_case__("Test 3",
                               [4, 4, 4, 1, 4],
                               [[], [1], [4], [1, 4], [4, 4], [1, 4, 4], [4, 4, 4], [1, 4, 4, 4],[4, 4, 4, 4],  [1, 4, 4, 4, 4]
                                ])

