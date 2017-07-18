from src.base.test_cases import TestCases
from src.structures.random_list_node import RandomListNode

class CpListWRandomPointersTestCases(TestCases):

    def __init__(self):
        super(CpListWRandomPointersTestCases, self).__init__()
        head_one = self.__get_test_one__()
        self.__add_test_case__("Test 1", (head_one), head_one)
        self.__add_test_case__("Test 2", (None), None)


    def __get_test_one__(self):
        node_list = []
        for i in range(0, 6):
            node_list.append(RandomListNode(i))

        for i in range(0, 5):
            node_list[i].next = node_list[i + 1]

        node_list[0].random = node_list[3]
        node_list[1].random = node_list[2]
        node_list[3].random = node_list[5]
        node_list[4].random = node_list[2]
        return node_list[0]

if __name__ == '__main__':
    test = CpListWRandomPointersTestCases()