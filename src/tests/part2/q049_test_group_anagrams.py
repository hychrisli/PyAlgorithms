from src.base.test_cases import TestCases

class GroupAnagramsTestCases(TestCases):

    def __init__(self):
        super(GroupAnagramsTestCases, self).__init__()
        self.__add_test_case__(
            'Test 1',
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [
                ["ate", "eat", "tea"],
                ["nat", "tan"],
                ["bat"]
            ]
        )