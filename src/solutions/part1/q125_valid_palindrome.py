from src.base.solution import Solution
from src.tests.part1.q125_test_valid_palindrome import ValidPalindromeTestCases

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome. 

"""


class ValidPalindrome(Solution):
    def print_output(self, output):
        super(ValidPalindrome, self).print_output(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return ValidPalindromeTestCases()

    def run_test(self, input):
        return self.isPalindrome(input)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        si, ei = 0, len(s) - 1

        while si < ei:
            if not s[ei].isalnum():
                ei -= 1
                continue

            if not s[si].isalnum():
                si += 1
                continue

            if s[si] != s[ei]:
                return False

            ei -= 1
            si += 1

        return True


if __name__ == '__main__':
    sol = ValidPalindrome()
    sol.run_tests()