from src.base.solution import Solution
from src.tests.part2.q187_test_repeat_dna_seq import RepeatDnaSeqTestCases


class RepeatDnaSeq(Solution):
    def run_test(self, input):
        return self.findRepeatedDnaSequences(input)

    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def gen_test_cases(self):
        return RepeatDnaSeqTestCases()

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        n = len(s)
        lkp, res = dict(),[]
        if n < 11: return res

        for i in xrange(n-9):
            sub = s[i:i+10]
            lkp[sub] = lkp.get(sub, 0) + 1
            if lkp[sub] == 2: res.append(sub)

        return res



if __name__ == '__main__':
    sol = RepeatDnaSeq()
    sol.run_tests()