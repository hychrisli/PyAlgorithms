

class MinHeap:

    def __init__(self, lst):
        self.lst = lst
        self.n = len(lst)


    def min_heapify(self, i):
        li, ri, imin = 2*i + 1, 2*(i+1), i

        if li < self.n and self.lst[li] < self.lst[imin]:
            imin = li
        if ri < self.n and self.lst[ri] < self.lst[imin]:
            imin = ri

        if imin != i:

            tmp = self.lst[i]
            self.lst[i] = self.lst[imin]
            self.lst[imin] = tmp

            self.min_heapify(imin)


if __name__ == '__main__':
    heap1 = MinHeap([7, 2, 3, 4, 5, 6])
    heap1.min_heapify(0)
    print(heap1.lst)