from src.base.solution import Solution
from src.tests.part2.q004_test_median_two_sorted_arrays import MedianTwoSortedArraysTestCases

class MedianTwoSortedArrays(Solution):
    def gen_test_cases(self):
        return MedianTwoSortedArraysTestCases()

    def run_test(self, input):
        return self.findMedianSortedArrays(input[0], input[1])

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        is_odd, imid = ( m + n ) % 2 == 1, (m + n) / 2 + 1
        i, j, curval, preval, = 0, 0, 0, 0

        while i < m and j < n and i + j < imid:
            preval = curval
            if nums1[i] < nums2[j]:
                curval = nums1[i]
                i += 1
            else:
                curval = nums2[j]
                j += 1
            print((i, j, imid, preval, curval))

        while i < m and i + j < imid:
            preval = curval
            curval = nums1[i]
            i += 1

        while j < n and i + j < imid:
            preval = curval
            curval = nums2[j]
            j += 1

        return curval if is_odd else (curval + preval) / 2.0

if __name__ == '__main__':
    sol = MedianTwoSortedArrays()
    sol.run_tests()