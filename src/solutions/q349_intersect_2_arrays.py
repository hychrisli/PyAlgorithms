from src.base.solution import Solution
from src.tests.q349_test_intersect_2_arrays import Intersect2ArraysTestCases

class Intersect2Arrays(Solution):
    def print_output(self, output):
        super(Intersect2Arrays, self).print_output(output)

    def run_test(self, input):
        return self.intersection(input[0], input[1])

    def gen_test_cases(self):
        return Intersect2ArraysTestCases()

    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        """ 
        Type <type 'set'>: Not implemented

        set1 = set(nums1)
        set2 = set(nums2)
        return set1.intersection(set2)
        """

        bdict = dict()
        idict = dict()

        for num in nums1:
            bdict[num] = 1

        for num in nums2:
            if num in bdict:
                idict[num] = 1

        return idict.keys()




if __name__ == '__main__':
    sol = Intersect2Arrays()
    sol.run_tests()