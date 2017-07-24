from src.base.solution import Solution
from src.tests.part2.q451_test_sort_char_by_freq import SortCharByFreqTestCases

class SortCharByFreq(Solution):
    def verify_output(self, test_output, output):
        return test_output in set(output)

    def gen_test_cases(self):
        return SortCharByFreqTestCases()

    def run_test(self, input):
        return self.frequencySort(input)

    def frequencySort_v(self, s):
        """
        :type s: str
        :rtype: str
        """
        import heapq
        acc, n = dict(), len(s)
        buckets = [[] for _ in xrange(n + 1)]

        for ch in s:
            acc[ch] = acc.get(ch, 0) + 1

        for (key, val) in acc.iteritems():
            buckets[val].append(key * val)

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import heapq

        acc, n, pq = dict(), len(s), []

        for ch in s:
            acc[ch] = acc.get(ch, 0) + 1

        for key in acc:
            pq.append((- acc[key], key))

        heapq.heapify(pq)

        res = ""
        while pq:
            val = heapq.heappop(pq)
            res += (- val[0]) * val[1]

        return res


    def frequencySort_v1(self, s):
        """
        :type s: str
        :rtype: str
        """
        acc, n = dict(), len(s)
        buckets = [[] for _ in xrange(n+1)]

        for ch in s:
            acc[ch] = acc.get(ch, 0) + 1

        for key in acc:
            buckets[acc[key]].append(key * acc[key])

        for i in xrange(n+1):
            buckets[i] = ''.join(buckets[i])

        return ''.join(buckets[::-1])


if __name__ == '__main__':
    sol = SortCharByFreq()
    sol.run_tests()
