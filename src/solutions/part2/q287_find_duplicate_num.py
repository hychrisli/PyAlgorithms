from src.base.solution import Solution
from src.tests.part2.q287_test_find_duplicate_num import FindDuplicateNumTestCases

class FindDuplicateNum(Solution):
    def gen_test_cases(self):
        return FindDuplicateNumTestCases()

    def run_test(self, input):
        return self.findDuplicate(input)

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]

        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]

        lead = fast
        follow = 0

        while lead != follow:
            lead = nums[lead]
            follow = nums[follow]
            # print (lead, follow)

        return lead


if __name__ == '__main__':

    sol = FindDuplicateNum()
    sol.run_tests()