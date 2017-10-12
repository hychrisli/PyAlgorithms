from src.base.solution import Solution
from src.tests.part2.q081_test_rotated_search_ii import RotatedSearchIiTestCases

class RotatedSearchIi(Solution):
    def gen_test_cases(self):
        return RotatedSearchIiTestCases()

    def run_test(self, input):
        return self.search(input[0], input[1])


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        si, ei = 0, len(nums) - 1
        while si <= ei:
            mid = (si + ei) / 2
            if target == nums[mid]:
                return True

            while si < mid and nums[si] == nums[mid]:
                si += 1

            if nums[si] <= nums[mid]:
                # left is ordered
                if nums[si] <= target < nums[mid]:
                    ei = mid - 1
                else:
                    si = mid + 1
            else:
                # right is ordered
                if nums[mid] < target <= nums[ei]:
                    si = mid + 1
                else:
                    ei = mid - 1

        return False


    def search_v1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        si, ei = 0, len(nums) - 1

        while si <= ei:
            mid = (si + ei) / 2
            print (si, ei, mid)

            if target == nums[mid]:
                return True

            if nums[si] < nums[ei]:
                # Not rotated
                if target < nums[mid]:
                    ei = mid - 1
                else:
                    si = mid + 1
            elif nums[si] < nums[mid]:
                # largest value on the right
                if target >= nums[si] and target < nums[mid]:
                    ei = mid - 1
                else:
                    si = mid + 1
            elif nums[si] > nums[mid]:
                # largest value on the left
                if target <= nums[ei] and target > nums[mid]:
                    si = mid + 1
                else:
                    ei = mid - 1
            else:
                # too many duplicates to decide
                prob = mid
                while prob > si and nums[prob] == nums[si]:
                    prob -= 1
                if nums[prob] == nums[si]:
                    si = mid + 1
                else:
                    ei = prob


        return False


if __name__ == '__main__':
    sol = RotatedSearchIi()
    sol.run_tests()