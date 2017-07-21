

class MaxHeap:

    def __init__(self, lst):
        self.lst = lst
        self.n = len(lst)

    def max_heapify(self, i):

        li, ri, idxmax = 2*i+1, 2*(i+1), i

        if li < self.n and self.lst[li] > self.lst[idxmax]:
            idxmax = li
        if ri < self.n and self.lst[ri] > self.lst[idxmax]:
            idxmax = ri

        if idxmax != i:
            tmp = self.lst[i]
            self.lst[i] = self.lst[idxmax]
            self.lst[idxmax] = tmp

            self.max_heapify(idxmax)

    def max_heapify_iter(self, i):


        while i < self.n:

            li, ri, idxmax = 2*i+1, 2*(i+1), i

            if li < self.n and self.lst[li] > self.lst[idxmax]:
                idxmax = li
            if ri < self.n and self.lst[ri] > self.lst[idxmax]:
                idxmax = ri

            if idxmax == i: break

            tmp = self.lst[i]
            self.lst[i] = self.lst[idxmax]
            self.lst[idxmax] = tmp
            i = idxmax

    def build_max_heap(self):
        print self.n/2
        for i in xrange(self.n/2, -1, -1):
            self.max_heapify(i)
            print(self.lst)


    def heap_sort(self):
        pass

if __name__ == '__main__':
    heap1 = MaxHeap([5,4,6,2,1])
    heap1.max_heapify_iter(0)
    print(heap1.lst)
    # result: [6, 4, 5, 2, 1]

    heap2 = MaxHeap([27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
    heap2.max_heapify(2)
    print(heap2.lst)
    # Result [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]

    heap3 = MaxHeap([1,2,3,5,6,7,8,9,10,11])
    heap3.build_max_heap()
    print(heap3.lst)