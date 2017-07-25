from src.base.solution import Solution
from src.tests.part2.q324_test_wiggle_sort_ii import WiggleSortIiTestCases

"""
324. Wiggle Sort II

https://leetcode.com/problems/wiggle-sort-ii/#/description

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

"""

class WiggleSortIi(Solution):
    def verify_output(self, test_output, output):
        n = len(output)
        m = n / 2
        toe, too, oe, oo = [], [], [], []
        for i in xrange(m):
            if i * 2 < n:
                toe.append(test_output[i*2])
                oe.append(output[i*2])

            if i * 2 + 1 < n:
                too.append(test_output[i*2+1])
                oo.append(output[i*2+1])

        return set(toe) == set(oe) and set(too) == set(oo)


    def run_test(self, input):
        return self.wiggleSort(input)

    def gen_test_cases(self):
        return WiggleSortIiTestCases()

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

        return nums

if __name__ == '__main__':

    sol = WiggleSortIi()
    sol.run_tests()