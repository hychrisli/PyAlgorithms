from src.base.solution import Solution
from src.tests.part2.q049_test_group_anagrams import GroupAnagramsTestCases

"""
https://leetcode.com/problems/group-anagrams/#/submissions/1

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.


"""

class GroupAnagrams(Solution):
    def verify_output(self, test_output, output):

        res1 = set(['-'.join(sorted(x)) for x in test_output])
        res2 = set(['-'.join(sorted(y)) for y in output])
        print(res1)
        print(res2)
        return res1 == res2

    def gen_test_cases(self):
        return GroupAnagramsTestCases()

    def print_output(self, output):
        for lst in output:
            lst.sort()
            print(lst)

    def run_test(self, input):
        return self.groupAnagrams(input)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        grouplkp = dict()
        self.keylkp = dict()

        for s in strs:

            key = ''.join(sorted(s))
            if key in grouplkp:
                grouplkp[key].append(s)
            else:
                grouplkp[key] = [s]

        return grouplkp.values()


if __name__ == '__main__':
    sol = GroupAnagrams()
    sol.run_tests()