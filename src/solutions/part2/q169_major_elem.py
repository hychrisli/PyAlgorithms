from src.base.solution import Solution
from src.tests.part2.q169_test_major_elem import MajorElemTestCases

class MajorElem(Solution):
    def run_test(self, input):
        return self.majorityElement(input)

    def gen_test_cases(self):
        return MajorElemTestCases()

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        candid, cnt = "", 0

        for num in nums:
            if candid == num:
                cnt += 1
            elif cnt == 0:
                candid, cnt = num, 1
            else:
                cnt -= 1

        return candid



if __name__ == '__main__':
    sol = MajorElem()
    sol.run_tests()