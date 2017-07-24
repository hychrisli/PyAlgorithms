from src.base.test_cases import TestCases

class SortCharByFreqTestCases(TestCases):

    def __init__(self):

        super(SortCharByFreqTestCases, self).__init__()
        self.__add_test_case__('Test 1', 'tree', ['eetr', 'eert'])
        self.__add_test_case__('Test 2', 'cccaaa', ['cccaaa', 'aaaccc'])
        self.__add_test_case__('Test 3', 'Aabb', ['bbAa', 'bbaA'])
        self.__add_test_case__('Test 4', 'eeeee', ['eeeee'])
