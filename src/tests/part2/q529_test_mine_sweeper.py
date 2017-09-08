from src.base.test_cases import TestCases


class MineSweeperTestCases(TestCases):
    def __init__(self):
        super(MineSweeperTestCases, self).__init__()
        self.__add_test_case__('Test 1',
                               ([['E', 'E', 'E', 'E', 'E'],
                                 ['E', 'E', 'M', 'E', 'E'],
                                 ['E', 'E', 'E', 'E', 'E'],
                                 ['E', 'E', 'E', 'E', 'E']], [3, 0]),

                               [['B', '1', 'E', '1', 'B'],
                                ['B', '1', 'M', '1', 'B'],
                                ['B', '1', '1', '1', 'B'],
                                ['B', 'B', 'B', 'B', 'B']]
                               )

        self.__add_test_case__('Test 2',
                               ([['B', '1', 'E', '1', 'B'],
                                 ['B', '1', 'M', '1', 'B'],
                                 ['B', '1', '1', '1', 'B'],
                                 ['B', 'B', 'B', 'B', 'B']], [1, 2]),

                               [['B', '1', 'E', '1', 'B'],
                                ['B', '1', 'X', '1', 'B'],
                                ['B', '1', '1', '1', 'B'],
                                ['B', 'B', 'B', 'B', 'B']]
                               )

        self.__add_test_case__('Test 3',
                               ([['E', 'E', 'E', 'E', 'E'],
                                 ['E', 'E', 'M', 'E', 'E'],
                                 ['E', 'M', 'E', 'M', 'E'],
                                 ['E', 'E', 'E', 'E', 'E']], [0, 2]),

                               [['E', 'E', '1', 'E', 'E'],
                                ['E', 'E', 'M', 'E', 'E'],
                                ['E', 'M', 'E', 'M', 'E'],
                                ['E', 'E', 'E', 'E', 'E']]
                               )

        self.__add_test_case__('Test 4',
                               ([['E', 'E', 'E', 'E', 'E'],
                                 ['E', 'E', 'M', 'E', 'E'],
                                 ['E', 'M', 'E', 'M', 'E'],
                                 ['E', 'E', 'E', 'E', 'E']], [0, 0]),

                               [['B', '1', 'E', 'E', 'E'],
                                ['1', '2', 'M', 'E', 'E'],
                                ['E', 'M', 'E', 'M', 'E'],
                                ['E', 'E', 'E', 'E', 'E']]
                               )
