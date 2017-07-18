from src.base.test_cases import TestCases

class HeatersTestCases(TestCases):

    def __init__(self):
        super(HeatersTestCases, self).__init__()
        self.__add_test_case__("Example 1", ([1,2,3],[2]), (1))
        self.__add_test_case__("Example 2", ([1,2,3,4], [1,4]),(1))
        self.__add_test_case__("Test 3", ([1, 2, 3, 4, 5, 89, 90, 91], [3, 89]), (2))
        self.__add_test_case__("Test 4", ([474833169, 264817709, 998097157, 817129560], [197493099, 404280278, 893351816, 505795335]), (104745341))

