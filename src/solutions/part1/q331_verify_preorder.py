from src.base.solution import Solution
from src.tests.part2.q331_test_verify_preorder import VerifyPreOrderTestCases


class VerifyPreOrder(Solution):
    def gen_test_cases(self):
        return VerifyPreOrderTestCases()

    def run_test(self, input):
        return self.isValidSerialization(input)


    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(",")
        diff = 1

        for node in nodes:
            diff -= 1
            if diff < 0: return False
            if node != '#': diff += 2

        return diff == 0


    def isValidSerialization_v1(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder == '#': return True

        lkp, stk, idx, parent = dict(), [], 0, None
        vals = preorder.split(",")

        for i in xrange(len(vals)):
            # print("------ " + str((i, vals[i])) + " --------")
            # print(stk)
            # print(lkp)

            if vals[i] == '#':
                if parent in lkp:
                    lkp[parent] += 1
                else:
                    return False
            else:

                if parent != None:
                    lkp[parent] += 1
                elif i:
                    return False
                lkp[i] = 0
                stk.append(i)

            while stk and lkp[stk[-1]] == 2:
                stk.pop()

            parent = stk[-1] if stk else None

        return False if stk else True


if __name__ == '__main__':
    sol = VerifyPreOrder()
    sol.run_tests()