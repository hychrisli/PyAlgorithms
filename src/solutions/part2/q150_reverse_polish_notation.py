from src.base.solution import Solution
from src.tests.part2.q150_test_reverse_polish_notation import ReversePolishNotationTestCases

class ReversePolishNotation(Solution):
    def run_test(self, input):
        return self.evalRPN(input)

    def gen_test_cases(self):
        return ReversePolishNotationTestCases()

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        ops = \
            {'+': lambda x, y: x + y,
             '-': lambda x, y: x - y,
             '*': lambda x, y: x * y,
             '/': lambda x, y: int(float(val2) / val1)}

        for s in tokens:
            if s in ops:
                val1 = stk.pop()
                val2 = stk.pop()
                val = ops[s](val2, val1)
                stk.append(val)
                # print(stk)
            else:
                stk.append(int(s))

        return stk[0]


if __name__ == '__main__':
    sol = ReversePolishNotation()
    sol.run_tests()