from src.base.test_cases import TestCases

class Intersect2ArraysTestCases(TestCases):

    def __init__(self):
        super(Intersect2ArraysTestCases, self).__init__()
        self.__add_test_case__("Example 1", ([1, 2, 2, 1], [2, 2]), ([2]))
        self.__add_test_case__("Example 1", ([1,2,3,4,8,2], [2,5,9,8]), ([2,8]))

