from src.base.solution import Solution
from src.tests.part1.q080_test_rm_duplicates_sorted_array_ii import RmDuplicatesSortedArrayIITestCases

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/#/description


Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesn't matter what you leave beyond the new length.
''

"""


class RmDuplicatesSortedArrayII(Solution):
    def run_test(self, input):
        return self.removeDuplicates(input)

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return RmDuplicatesSortedArrayIITestCases()

    def removeDuplicates(self, nums):

        i = 0

        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1

        return i


    def removeDuplicates_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diff, cnt, li, fi, n = 0, 2, 0, 0, len(nums)
        curval = nums[0] if n > 0 else None


        while li < n:

            if nums[li] != curval:
                cnt = 2
                curval = nums[li]

            if cnt > 0:
                if nums[li] == curval:
                    cnt -= 1
                nums[fi] = nums[fi + diff]
                fi += 1
            else:
                diff += 1
            li += 1


        # print(('fi', fi, nums[:fi]))

        return fi



if __name__ == '__main__':
    sol = RmDuplicatesSortedArrayII()
    sol.run_tests()