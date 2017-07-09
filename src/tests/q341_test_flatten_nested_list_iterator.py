from src.base.solution import TestCases

class FlattenNestedListIteratorTestCases(TestCases):

    def __init__(self):

        super(FlattenNestedListIteratorTestCases, self).__init__()
        self.__add_test_case__("Test 1", [[1,1],2,[1,1]], [1,1,2,1,1])
        self.__add_test_case__("Test 2", [1,[4,[6]]], [1,4,6])
        self.__add_test_case__("Test 3", [[[[1]]]], [1])
        self.__add_test_case__("Test 4", [[],[]], [])