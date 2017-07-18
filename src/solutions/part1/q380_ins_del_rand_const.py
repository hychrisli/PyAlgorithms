import random

from src.base.solution import Solution
from src.tests.part1.q380_test_ins_del_rand_const import InsDelRandConstTestCases
from src.utility.constants import INSERT, REMOVE

"""
https://leetcode.com/problems/insert-delete-getrandom-o1/#/description

esign a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

"""


class InsDelRandConst(Solution):

    def __init__(self):
        super(InsDelRandConst, self).__init__()
        self.rset = RandomizedSet()

    def run_test(self, input):
        if input[0] == INSERT:
            return self.rset.insert(input[1])
        elif input[0] == REMOVE:
            return self.rset.remove(input[1])
        else:
            return self.rset.getRandom() in input[1]

    def print_output(self, output):
        print(output)

    def verify_output(self, test_output, output):
        return test_output == output

    def gen_test_cases(self):
        return InsDelRandConstTestCases()



class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.l = []
        self.idx = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        if val not in self.d:
            self.l.append(val)
            self.d[val] = self.idx
            self.idx += 1
            return True

        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """

        if val in self.d:

            last_val = self.l.pop()
            if last_val != val:

                self.l[self.d[val]] = last_val
                self.d[last_val] = self.d[val]

            self.d.pop(val)
            self.idx -= 1
            return True

        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.l[random.randint(0, self.idx - 1)]


if __name__ == '__main__':
    sol = InsDelRandConst()
    sol.run_tests()