from max_heap import MaxHeap

class MaxPriorityQueues:

    def __init__(self, lst, k):
        self.heap = MaxHeap(lst)
        self.heap.build_max_heap()
        self.k = k

    def heap_max(self):
        return self.heap.elems[0]

    def extract_max(self):
        if self.k < 1: return None

        val = self.heap.elems[0]
        self.k -= 1
        self.heap.elems[0] = self.heap.elems[self.k]
        self.heap.max_heapify(0)
        return val

    def increase_key(self, i, key):
        pass

    def insert(self, key):
        self.k += 1
        if self.k >= self.heap.n:
            self.heap.elems.append(key)
            self.heap.n += 1
        else:
            self.heap.elems[self.k] = key

        i = (self.k - 1) / 2
        while i:
            self.heap.max_heapify(i)
            i /= 2
        self.heap.max_heapify(0)

if __name__ == '__main__':
    q1 = MaxPriorityQueues([6,5,4,3,2,1], 5)
    print(q1.heap_max())

    q2 = MaxPriorityQueues([1,2,3,4,5], 5)
    print(q2.extract_max())
    print(q2.heap.elems)

    q3 = MaxPriorityQueues([1,2,3,4,5], 5)
    print(q3.heap.elems)
    q3.insert(7)
    print(q3.heap.elems)