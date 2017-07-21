from src.base.solution import Solution
from src.tests.part2.q017_test_phone_letters_combine import PhoneLettersCombineTestCases
import collections

class PhoneLettersCombine(Solution):
    def gen_test_cases(self):
        return PhoneLettersCombineTestCases()

    def run_test(self, input):
        return self.letterCombinations(input)

    def verify_output(self, test_output, output):
        return set(test_output) == set(output)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.lkp = [
            [' '], [],['a','b','c'], ['d','e','f'],
            ['g','h','i'], ['j','k','l'], ['m','n','o'],
            ['p','q','r','s'],['t','u','v'],['w','x','y','z']
        ]
        self.digits = digits
        self.n = len(digits)
        if not self.n: return []
        return self.combine([""], 0)

    def combine(self, lst, idx):
        if idx == self.n: return lst
        res = []
        val = int(self.digits[idx])
        for str in lst:
            for ch in self.lkp[val]:
                res.append(str + ch)
        if not res: res = lst
        return self.combine(res, idx+1)

if __name__ == '__main__':
    sol = PhoneLettersCombine()
    sol.run_tests()