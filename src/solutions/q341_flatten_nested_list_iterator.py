from src.base.solution import Solution
from src.tests.q341_test_flatten_nested_list_iterator import FlattenNestedListIteratorTestCases

"""
https://leetcode.com/problems/flatten-nested-list-iterator/#/description

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6]. 

"""

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for item in nestedList[::-1]:
            self.stack.append(item)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        # print(self.stack)

        while self.stack and isinstance(self.stack[-1], list):
            sublst = self.stack.pop()
            print((self.stack, sublst, len(sublst)))
            for item in sublst[::-1]:
                self.stack.append(item)

        if self.stack: return True
        else: return False

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())


class FlattenNestedListIterator(Solution):
    def print_output(self, output):
        super(FlattenNestedListIterator, self).print_output(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return FlattenNestedListIteratorTestCases()

    def run_test(self, input):
        i, v = NestedIterator(input), []
        while i.hasNext(): v.append(i.next())
        return v


if __name__ == '__main__':
    sol = FlattenNestedListIterator()
    sol.run_tests()