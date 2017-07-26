from src.base.test_cases import TestCases

class CourseScheduleIiTestCases(TestCases):

    def __init__(self):
        super(CourseScheduleIiTestCases, self).__init__()
        self.__add_test_case__('Test 1', (2, [[1,0]]), ([0, 1],))
        self.__add_test_case__('Test 2', (4, [[1,0],[2,0],[3,1],[3,2]]), ([0, 1, 2, 3], [0,2,1,3]))
        self.__add_test_case__('Test 3', (4, [[1,0],[2,0],[3,1],[2,3]]), ([0, 1, 3, 2], ))
        self.__add_test_case__('Test 4', (4, [[1, 0], [1, 2], [3, 1], [2, 3]]), ([],))
        self.__add_test_case__('Test 5', (1, []), ([0],))
        self.__add_test_case__('Test 6', (2, []), ([1,0], [0,1]))
        self.__add_test_case__('Test 7', (3, [[1, 0]]), ([0, 1, 2], [0, 2, 1]))

        