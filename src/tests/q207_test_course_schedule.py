from src.base.test_cases import TestCases


class CourseScheduleTestCases(TestCases):
    def __init__(self):
        super(CourseScheduleTestCases, self).__init__()
        self.__add_test_case__("Test 1", (2, [[1, 0], [0, 1]]), (False))
        self.__add_test_case__("Test 2", (2, [[1, 0]]), (True))
        self.__add_test_case__("Test 3", (4, [[0, 1], [2, 3], [3, 1], [1, 2]]), (False))
        self.__add_test_case__("Test 4", (4, [[0, 1], [2, 3], [1, 3], [1, 2]]), (True))
        self.__add_test_case__("Test 5", (3, [[1,0],[2,1]]), (True))