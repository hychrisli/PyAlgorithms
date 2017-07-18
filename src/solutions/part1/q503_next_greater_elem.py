from src.base.solution import Solution
from src.tests.part1.q503_test_next_greater_elem import NextGreaterElemTestCases

class NextGreaterElem(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return NextGreaterElemTestCases()

    def run_test(self, input):
        return self.nextGreaterElements(input)

    def print_output(self, output):
        print(output)

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack, res = [], [-1] * n


        for idx in xrange(n * 2):

            i = idx % n

            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]

            stack.append(i)

        return res

# e.g. [1,2,1]
# n = 3
# i = 4
# idx = 1
# stack = []
# res = [2,-1,2]


if __name__ == '__main__':
    sol = NextGreaterElem()
    sol.run_tests()