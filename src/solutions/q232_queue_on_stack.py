from src.base.solution import Solution
from src.tests.q232_test_queue_on_stack import QueueOnStackTestCases


class QueueOnStack(Solution):

    def gen_test_cases(self):
        return QueueOnStackTestCases()

    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        print(output)

    def run_test(self, input):
        q = MyQueue()
        for i in input:
            q.push(i)
        return (q.pop(), q.peek(), q.empty())


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enq = []
        self.deq = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.enq.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None

        return self.deq.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None

        return self.deq[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """

        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())

        return not self.deq

if __name__ == '__main__':
    sol = QueueOnStack()
    sol.run_tests()