from src.base.solution import Solution
from src.tests.part2.q238_test_array_product import ArrayProductTestCases

class ArrayProduct(Solution):
    def run_test(self, input):
        return self.productExceptSelf(input)

    def gen_test_cases(self):
        return ArrayProductTestCases()

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]

        for i in xrange(len(nums) - 1):
            res.append(res[-1] * nums[i])

        pp = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] *= pp
            pp *= nums[i]

        return res


    def productExceptSelf_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nlen, left, right, res = len(nums), [1], [1], []

        for i in xrange(nlen - 1):
            left.append(left[-1] * nums[i])
            right.append(right[-1] * nums[nlen-i-1])

        for i in xrange(nlen):
            res.append(left[i] * right[nlen-i-1])

        return res

if __name__ == '__main__':
    sol = ArrayProduct()
    sol.run_tests()