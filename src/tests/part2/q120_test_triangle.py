from src.base.test_cases import TestCases

class TriangleTestCases(TestCases):

    def __init__(self):

        super(TriangleTestCases, self).__init__()
        self.__add_test_case__('Test 1',
                               [
                                   [2],
                                   [3, 4],
                                   [6, 5, 7],
                                   [4, 1, 8, 3]
                               ],
                                11
                               )
        