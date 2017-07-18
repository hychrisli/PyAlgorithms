from src.base.solution import Solution
from src.tests.part2.q461_test_hamming_dist import HammingDistTestCases

class HammingDist(Solution):
    def run_test(self, input):
        return self.hammingDistance(input[0], input[1])

    def print_output(self, output):
        print(output)

    def gen_test_cases(self):
        return HammingDistTestCases()

    def verify_output(self, test_output, output):
        return test_output == output

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')



if __name__ == '__main__':
    sol = HammingDist()
    sol.run_tests()