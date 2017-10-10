from src.base.test_cases import TestCases


class DecodeStrTestCases(TestCases):

    def __init__(self):
        super(DecodeStrTestCases, self).__init__()
        self.__add_test_case__("Test 1", "3[a]2[bc]", "aaabcbc")
        self.__add_test_case__("Test 2", "3[a2[c]]", "accaccacc")
        self.__add_test_case__("Test 3", "2[abc]3[cd]ef", "abcabccdcdcdef")
        self.__add_test_case__("Test 4", "abc", "abc")
        self.__add_test_case__("Test 5", "3[c]4[d]", "cccdddd")
        self.__add_test_case__("Test 6", "ab3[e]", "abeee")
        self.__add_test_case__("Test 7", "a2[e3[v]cg]d", "aevvvcgevvvcgd")
        self.__add_test_case__("Test 8", "2[2[b]]", "bbbb")
        self.__add_test_case__("Test 9", "2[2[2[b]]]", "bbbbbbbb")


