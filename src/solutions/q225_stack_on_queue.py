from src.base.solution import Solution
from src.tests.q225_test_stack_on_queue import StackOnQueueTestCases
import collections


class StackOnQueue(Solution):

    def gen_test_cases(self):
        return StackOnQueueTestCases()

    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        q = MyStack()
        for i in input:
            q.push(i)
        return (q.pop(),q.top(),q.empty())


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """


    def top(self):
        """
        Get the top element.
        :rtype: int
        """


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """


if __name__ == '__main__':
    sol = StackOnQueue()
    sol.run_tests()