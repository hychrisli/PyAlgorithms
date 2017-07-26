from src.base.solution import Solution
from src.tests.part2.q146_test_lru_cache import LruCacheTestCases


class LruCacheRunner(Solution):
    def print_output(self, output):
        super(LruCacheRunner, self).print_output(output)

    def run_test(self, input):
        self.run()
        return True

    def gen_test_cases(self):
        return LruCacheTestCases()

    def run(self):
        print("Test 1")
        lc1 = LRUCache(2)
        lc1.put(1,10)
        lc1.put(2,20)
        print("get 1: " + str(lc1.get(1)))
        lc1.put(3,30)
        print("get 2: " + str(lc1.get(2)))
        lc1.put(4,40)
        print("get 1: " + str(lc1.get(1)))
        print("get 3: " + str(lc1.get(3)))
        print("get 4: " + str(lc1.get(4)))


        print("Test 2")
        lc2 = LRUCache(1)
        lc2.put(2,1)
        print("get 2: " + str(lc2.get(2)))

        print("\nTest 3\n")
        lc3 = LRUCache(1)
        lc3.put(2, 1)
        print("get 2: " + str(lc3.get(2)))
        lc3.put(3,2)
        print("get 2: " + str(lc3.get(2)))
        print("get 3: " + str(lc3.get(3)))

        print("\nTest 4\n")
        lc4 = LRUCache(2)
        lc4.put(2,1)
        lc4.put(1,1)
        lc4.put(2,3)
        lc4.put(4,1)

        print("\nTest 5\n")
        lc5 = LRUCache(3)
        lc5.put(1,1)
        lc5.put(2,2)
        lc5.put(3,3)
        lc5.put(4,4)
        print(lc5.get(4))
        print(lc5.get(3))
        print(lc5.get(2))
        print(lc5.get(1))
        lc5.put(5,5)

class DoubleListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def to_str(self):
        pt, res = self, []

        while pt:
            res.append(str(pt.val))
            pt = pt.next

        return ' -> '.join(res)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.lkp  = dict()
        self.next = None
        self.prev = None
        self.cnt = 0

        self.head = DoubleListNode(None)
        self.tail = DoubleListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lkp: return -1

        node = self.lkp[key]

        node.prev.next = node.next
        self.move_after_head(node)

        # print(self.head.to_str())

        return node.val[1]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.lkp:
            self.lkp[key].val = (key, value)
            self.move_after_head(self.lkp[key])
        else:
            node = DoubleListNode((key, value))

            self.insert_after_head(node)

            self.lkp[key] = node
            self.cnt += 1

            if self.cnt > self.capacity:

                last_key = self.tail.prev.val[0]
                self.tail.prev = self.tail.prev.prev
                # print(("last_key", last_key))
                self.tail.prev.next = self.tail
                self.lkp.pop(last_key)
                self.cnt -= 1

        # print(self.head.to_str())

    def insert_after_head(self, node):
        next_node = self.head.next
        node.next = next_node
        next_node.prev = node

        node.prev = self.head
        self.head.next = node

    def move_after_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insert_after_head(node)

if __name__ == '__main__':
    sol = LruCacheRunner()
    sol.run_tests()