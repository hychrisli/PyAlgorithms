

class QuickSort:

    def __init__(self, lst):
        self.lst = lst

    def sort(self, si, ei):
        if si < ei:
            mid = self.partition(si, ei)
            self.sort(si, mid - 1 )
            self.sort(mid + 1, ei)

    def partition(self, si, ei):
        x = self.lst[ei]
        k = si - 1

        for j in xrange(si, ei):
            if self.lst[j] <= x:
                k += 1
                self.lst[k], self.lst[j] = self.lst[j], self.lst[k]
        self.lst[k + 1], self.lst[ei] = self.lst[ei], self.lst[k + 1]
        return k + 1


if __name__ == '__main__':
    srt = QuickSort([2,8,7,1,3,5,6,4])
    srt.sort(0, 7)
    print(srt.lst)