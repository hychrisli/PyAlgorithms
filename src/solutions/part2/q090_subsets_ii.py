from src.base.solution import Solution
from src.tests.part2.q090_test_subsets_ii import SubsetsIiTestCases

class SubsetsIi(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def run_test(self, input):
        return self.subsetsWithDup(input)

    def gen_test_cases(self):
        return SubsetsIiTestCases()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res, cnt, pre = [[]], 0, nums[0]
        nums.append('#')

        for num in nums:
            # print (pre, num, cnt)
            if pre == num:
                cnt += 1
                continue

            tailsets, addset = [], []
            while cnt > 0:
                addset.append(pre)
                cnt -= 1
                # print(cnt, pre)
                for subset in res:

                    newset = subset + addset
                    tailsets.append(newset)

            res.extend(tailsets)
            pre, cnt = num, 1

        return res


if __name__ == '__main__':
    sol = SubsetsIi()
    sol.run_tests()