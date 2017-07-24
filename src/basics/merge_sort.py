

class MergeSort:

    def __init__(self, lst):
        self.lst = lst


    def sort(self):
        self.merge_sort(0, len(self.lst) - 1)

    def merge_sort(self, i, j):

        if i < j:
            mid = (i+j) / 2
            self.merge_sort(i, mid)
            self.merge_sort(mid+1, j)
            self.merge(i, mid, j)

    def merge(self, si, mi, ei):
        res = []
        i, j = si, mi + 1

        while i <= mi and j <= ei:
            if self.lst [i] > self.lst[j]:
                res.append(self.lst[j])
                j += 1
            else:
                res.append(self.lst[i])
                i += 1

        res.extend(self.lst[i:mi+1])
        res.extend(self.lst[j:ei+1])
        self.lst[si:ei+1] = res

if __name__ == '__main__':
    ms = MergeSort([3,4,5,2,9,10,8,2,1,12,14])
    ms.sort()
    print(ms.lst)