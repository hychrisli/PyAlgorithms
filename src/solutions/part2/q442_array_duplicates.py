from src.base.solution import Solution
from src.tests.part2.q442_test_array_duplicates import ArrayDuplicatesTestCases

class ArrayDuplicates(Solution):
    def gen_test_cases(self):
        return ArrayDuplicatesTestCases()

    def run_test(self, input):
        return self.findDuplicates(input)

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = []

        for num in nums:
            val = abs(num)

            if nums[val - 1] > 0:
                nums[val - 1] *= -1
            else:
                res.append(val)

        return res


if __name__ == '__main__':
    sol = ArrayDuplicates()
    sol.run_tests()