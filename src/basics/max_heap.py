

class MaxHeap:

    def __init__(self, lst):
        self.elems = lst
        self.n = len(lst)


    # Maintain the max heap features
    def max_heapify(self, i):

        li, ri, idxmax = 2*i+1, 2*(i+1), i

        if li < self.n and self.elems[li] > self.elems[idxmax]:
            idxmax = li
        if ri < self.n and self.elems[ri] > self.elems[idxmax]:
            idxmax = ri

        if idxmax != i:
            tmp = self.elems[i]
            self.elems[i] = self.elems[idxmax]
            self.elems[idxmax] = tmp

            self.max_heapify(idxmax)

    # Interatively heapify
    def max_heapify_iter(self, i):

        while i < self.n:

            li, ri, idxmax = 2*i+1, 2*(i+1), i

            if li < self.n and self.elems[li] > self.elems[idxmax]:
                idxmax = li
            if ri < self.n and self.elems[ri] > self.elems[idxmax]:
                idxmax = ri

            if idxmax == i: break

            self.swap(i,idxmax)
            i = idxmax

    # convert random list to heap
    def build_max_heap(self):
        # print self.n/2
        for i in xrange(self.n/2, -1, -1):
            self.max_heapify(i)
            # print(self.lst)


    def heap_sort(self):
        self.build_max_heap()
        for i in xrange(self.n - 1, 0, -1):
            self.swap(0, i)
            self.n -= 1
            self.max_heapify(0)

    def swap(self, i, j):
        tmp = self.elems[i]
        self.elems[i] = self.elems[j]
        self.elems[j] = tmp


if __name__ == '__main__':
    heap1 = MaxHeap([5,4,6,2,1])
    heap1.max_heapify_iter(0)
    print(heap1.elems)
    # result: [6, 4, 5, 2, 1]

    heap2 = MaxHeap([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
    heap2.max_heapify(2)
    print(heap2.elems)
    # Result [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]

    heap3 = MaxHeap([5,13, 2, 25, 7, 17, 20, 8, 4])
    heap3.build_max_heap()
    print(heap3.elems)

    heap4 = MaxHeap([1,2,3,5,6,7,8,9,9,9,9,10,11])
    heap4.heap_sort()
    print(heap4.elems)