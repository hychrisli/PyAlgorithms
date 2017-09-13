from src.base.solution import Solution
from src.tests.part2.q071_test_simplify_path import SimplifiyPathTestCases


class SimplifyPath(Solution):
    def gen_test_cases(self):
        return SimplifiyPathTestCases()

    def run_test(self, input):
        return self.simplifyPath(input)

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        lst, stk = path.split('/'), []

        for elem in lst:
            if elem == '..':
                if stk: stk.pop()
                else: continue
            elif elem == '.' or not elem:
                continue
            else:
                stk.append(elem)

        return '/' + '/'.join(stk)


if __name__ == '__main__':
    sol = SimplifyPath()
    sol.run_tests()