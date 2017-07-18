from src.base.solution import Solution
from src.tests.part1.q347_test_top_k_frequent_elements import TopKFreqElemTestCases

"""

https://leetcode.com/problems/top-k-frequent-elements/#/description

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

class TopKFreqElem(Solution):

    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def run_test(self, input):
        return self.topKFrequent(input[0], input[1])

    def gen_test_cases(self):
        return TopKFreqElemTestCases()

    def print_output(self, output):
        super(TopKFreqElem, self).print_output(output)

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        lkp = dict()
        for num in nums:
            lkp[num] = lkp.get(num, 0) + 1

        bucket = [None] * (len(nums) + 1)
        for (key, val) in lkp.items():
            if bucket[val] == None:
                bucket[val] = [key]
            else:
                bucket[val].append(key)

        res = []
        count = 0
        for lst in reversed(bucket):
            if lst != None:
                res += lst
                count += len(lst)

            if count >= k:
                break

        return res


if __name__ == '__main__':
    solution = TopKFreqElem()
    solution.run_tests()