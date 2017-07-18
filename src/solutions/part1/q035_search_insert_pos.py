import math

from src.base.solution import Solution
from src.tests.part1.p035_test_search_insert_pos import SearchInsertPosTestCases


class SearchInsertPos(Solution):
    def run_test(self, input):
        return self.searchInsert(input[0], input[1])

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return SearchInsertPosTestCases()


    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        si, ei = 0, len(nums) - 1

        while ei - si > 1:
            mid = (si + ei) / 2
            if target < nums[mid]:
                ei = mid
            else:
                si = mid

        if target <= nums[si]:
            return si
        elif target <= nums[ei]:
            return ei
        else:
            return ei + 1


    def searchInsert_recur(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        self.target = target
        return self.search(0, len(nums) - 1)

    def search(self, si, ei):
        if ei - si <= 1:
            if self.target <= self.nums[si]:
                return si
            elif self.target <= self.nums[ei]:
                return ei
            else:
                return ei + 1

        mid = int(math.floor((si + ei) / 2))
        if self.target < self.nums[mid]:
            return self.search(si, mid)
        else:
            return self.search(mid, ei)


if __name__ == '__main__':
    sol = SearchInsertPos()
    sol.run_tests()
