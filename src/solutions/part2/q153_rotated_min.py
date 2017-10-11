from src.base.solution import Solution
from src.tests.part2.q153_test_rotated_min import RotatedMinTestCases

class RotatedMin(Solution):
    def run_test(self, input):
        return self.findMin(input)

    def gen_test_cases(self):
        return RotatedMinTestCases()

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        si, ei = 0, len(nums) - 1

        while si < ei:
            # print((si, ei), (nums[si], nums[ei-1]))
            if nums[si] < nums[ei]:
                return nums[si]

            mid = (si+ei) / 2

            if nums[si] <= nums[mid]  :
                si = mid + 1
            else:
                ei = mid
        return nums[si]


if __name__ == '__main__':
    sol = RotatedMin()
    sol.run_tests()