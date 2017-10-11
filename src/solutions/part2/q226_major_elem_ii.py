from src.base.solution import Solution
from src.tests.part2.q226_test_major_elem_ii import MajorElemIiTestCases


class MajorElemIi(Solution):
    def run_test(self, input):
        return self.majorityElement(input)

    def gen_test_cases(self):
        return MajorElemIiTestCases()

    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candid1, candid2, cnt1, cnt2 = '0', '0', 0, 0

        for num in nums:

            if candid1 == num:
                cnt1 += 1
            elif candid2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                candid1, cnt1 = num, 1
            elif cnt2 == 0:
                candid2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            # print((candid1, cnt1), (candid2, cnt2))

        return [x for x in (candid1, candid2) if nums.count(x) > len(nums) / 3]




if __name__ == '__main__':
    sol = MajorElemIi()
    sol.run_tests()