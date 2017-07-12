from src.base.test_cases import TestCases

class HouseRobberTestCases(TestCases):

    def __init__(self):
        super(HouseRobberTestCases, self).__init__()
        self.__add_test_case__("Test 1", [1, 2, 3, 4, 5, 6], 12)
        self.__add_test_case__("Test 2", [1, 7, 1, 1, 8, 9,1, 1,0], 18)
        self.__add_test_case__("Test 3", [2,1,1,2], 4)
        self.__add_test_case__("Test 3", [3, 1, 1, 1, 3], 7)


